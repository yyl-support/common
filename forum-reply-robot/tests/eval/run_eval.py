"""RAG 检索质量离线评测入口(Phase 1)。

行为:
1. 从 eval_query_set 读全部 query。表为空则提示后退出。
2. 对每条 query 走当前 retrieval.backend,记录检索上下文、延迟、LLM 答案。
3. 对每条结果跑 4 个 deepeval 指标,Precision/Recall 在 GT 缺失时标记 skipped。
4. 结果全部落到 eval_retrieval_runs + eval_metric_scores 表。
5. 终端打印按 backend x metric 的汇总。

用法:
    python tests/eval/run_eval.py --run-tag baseline-2026-05-11
    python tests/eval/run_eval.py --run-tag smoke --dry-run    # 不跑指标,只验链路
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path
from typing import Mapping, Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _load_config() -> dict:
    """工程启动后会删掉 config.yaml,这里按优先级回退。"""
    from src.utils import load_config
    candidates = [
        "config/config.yaml",
        "config/config.yaml.local-bak",
        "config/config.yaml.startup-bak",
        "config/config.yaml.bak",
    ]
    for p in candidates:
        if Path(p).exists():
            cfg = load_config(p)
            if cfg:
                print(f"[config] 使用 {p}")
                return cfg
    raise SystemExit("未找到任何可用的 config.yaml;请在 config/ 下放置配置文件")


def _split_chunks(related_docs: str) -> list[str]:
    from src.ForumBot.data_processor import extract_json_blocks
    blocks = extract_json_blocks(related_docs or "")
    if isinstance(blocks, list) and blocks:
        labels = ["Entities(KG)", "Relationships(KG)", "Document Chunks(DC)"]
        return [f"{labels[i] if i < len(labels) else 'Block'}:\n{b}"
                for i, b in enumerate(blocks) if b]
    return [related_docs] if related_docs else [""]


def _call_llm(config: Mapping[str, Any], question: str, context_data: str,
              query_id: str) -> tuple[str, int]:
    from src.ForumBot.ai_processor import AIProcessor
    from src.ForumBot.data_processor import PROMPT_TEMPLATE
    system_prompt_text = PROMPT_TEMPLATE.format(history="", context_data=context_data)
    ai = AIProcessor(config)
    t0 = time.perf_counter()
    answer = ai.call_large_model(
        text=system_prompt_text,
        title="",
        user_question=question,
        topic_id=None,
        max_retries=2,
    )
    return answer or "", int((time.perf_counter() - t0) * 1000)


def _run_one(config, forum_client, row, run_tag, dry_run, judge):
    from tests.eval.db import insert_retrieval_run, insert_metric_score, connect
    from tests.eval.metrics import build_test_case, run_all_metrics

    query_id = row["query_id"]
    question = row["question"]
    backend = ((config.get("retrieval") or {}).get("backend") or "lightrag").lower()
    rcfg = config.get("retrieval", {}) or {}

    print(f"\n[{query_id}] backend={backend} question={question[:60]}")

    t0 = time.perf_counter()
    res = forum_client.rag_backend.query(
        question,
        top_k=rcfg["top_k"],
        chunk_top_k=rcfg["chunk_top_k"],
        enable_rerank=rcfg["enable_rerank"],
        only_need_context=rcfg.get("only_need_context", True),
        only_need_prompt=rcfg.get("only_need_prompt", False),
    )
    retrieval_latency = int((time.perf_counter() - t0) * 1000)
    related_docs = res.get("related_docs", "") or ""
    chunks = _split_chunks(related_docs)
    print(f"  retrieval: {len(related_docs)} chars, {len(chunks)} chunks, {retrieval_latency} ms")

    answer, answer_latency = "", None
    if not dry_run:
        answer, answer_latency = _call_llm(config, question, related_docs, query_id)
        print(f"  answer: {len(answer)} chars, {answer_latency} ms")

    with connect(config) as conn:
        run_id = insert_retrieval_run(
            conn,
            query_id=query_id, backend=backend, run_tag=run_tag,
            retrieval_context=related_docs, retrieval_chunks=chunks,
            actual_output=answer,
            retrieval_latency_ms=retrieval_latency,
            answer_latency_ms=answer_latency,
        )
        print(f"  run_id={run_id}")

        if dry_run or judge is None:
            print("  metrics: skipped (dry-run or no judge)")
            return

        tc = build_test_case(
            question=question, answer=answer, chunks=chunks,
            expected_output=row.get("expected_output"),
        )
        for mr in run_all_metrics(tc, judge_llm=judge):
            insert_metric_score(conn, run_id=run_id, **mr)
            if mr.get("error"):
                print(f"  - {mr['metric_name']}: ERROR {mr['error']}")
            else:
                print(f"  - {mr['metric_name']}: {mr['score']:.3f}"
                      f" (ok={mr['is_successful']})")


def _print_summary(config, run_tag):
    from tests.eval.db import connect, summarize_run_tag, summarize_latency
    with connect(config) as conn:
        print(f"\n=== 延迟汇总 run_tag={run_tag} ===")
        for row in summarize_latency(conn, run_tag):
            print(f"  {row['backend']:10s}  n={row['n']:3d}"
                  f"  retr_mean={row['retrieval_mean_ms']}ms"
                  f"  p50={row['retrieval_p50_ms']}ms"
                  f"  p95={row['retrieval_p95_ms']}ms"
                  f"  ans_mean={row['answer_mean_ms']}ms")
        print(f"\n=== 指标汇总 run_tag={run_tag} ===")
        for row in summarize_run_tag(conn, run_tag):
            mean = "--" if row["mean"] is None else f"{row['mean']:.3f}"
            p50 = "--" if row["p50"] is None else f"{row['p50']:.3f}"
            p95 = "--" if row["p95"] is None else f"{row['p95']:.3f}"
            print(f"  {row['backend']:10s}  {row['metric_name']:22s}"
                  f"  n={row['n']:3d}  mean={mean}  p50={p50}  p95={p95}"
                  f"  errs={row['errors']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-tag", required=True, help="本次评测的批次标签")
    ap.add_argument("--dry-run", action="store_true",
                    help="仅跑检索,不调 LLM 也不跑 deepeval")
    ap.add_argument("--limit", type=int, default=0, help="只跑前 N 条(调试)")
    args = ap.parse_args()

    config = _load_config()

    from src.ForumBot.forum_client import ForumClient
    from tests.eval.db import connect, load_query_set

    with connect(config) as conn:
        queries = load_query_set(conn)
    if not queries:
        print("eval_query_set 为空;请先插入 query(参考 scripts/insert_eval_queries.sql.tpl)")
        return 0
    if args.limit:
        queries = queries[:args.limit]
    print(f"[query] 共 {len(queries)} 条待评测")

    forum_client = ForumClient(config)

    judge = None
    if not args.dry_run:
        from tests.eval.judges.siliconflow_judge import build_judge_from_config
        judge = build_judge_from_config(config)
        print(f"[judge] model={judge.get_model_name()}")

    for row in queries:
        try:
            _run_one(config, forum_client, row, args.run_tag, args.dry_run, judge)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {row['query_id']}: {type(exc).__name__}: {exc}")

    _print_summary(config, args.run_tag)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
