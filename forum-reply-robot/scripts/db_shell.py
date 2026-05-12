"""独立的 DB 查询 CLI。

用法:
    python scripts/db_shell.py tables
    python scripts/db_shell.py show forum_topics --limit 10
    python scripts/db_shell.py sql "SELECT count(*) FROM forum_topics"
    python scripts/db_shell.py eval-report --run-tag baseline-2026-05-11

优先从 config/config.yaml 读连接;找不到时按顺序回退到 .local-bak / .startup-bak / .bak。
也支持 DB_URL 环境变量(postgresql://user:pass@host:port/db)。
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import psycopg2
from psycopg2.extras import RealDictCursor


CONFIG_CANDIDATES = [
    "config/config.yaml",
    "config/config.yaml.local-bak",
    "config/config.yaml.startup-bak",
    "config/config.yaml.bak",
]


def _connect() -> Any:
    dburl = os.environ.get("DB_URL")
    if dburl:
        return psycopg2.connect(dburl)
    import yaml
    for p in CONFIG_CANDIDATES:
        full = ROOT / p
        if not full.exists():
            continue
        with open(full, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
        db = cfg.get("database") or {}
        if not db.get("host"):
            continue
        print(f"# config: {p}", file=sys.stderr)
        return psycopg2.connect(
            host=db["host"], port=db["port"], database=db["database"],
            user=db["user"], password=db["password"],
            sslmode=db.get("sslmode", "disable"),
        )
    raise SystemExit("没有可用的数据库配置,请提供 config/config.yaml 或设置 DB_URL")


def _print_rows(rows: list[dict], max_width: int = 80) -> None:
    if not rows:
        print("(空)")
        return
    keys = list(rows[0].keys())
    widths = {k: min(max_width, max(len(k), *(len(str(r.get(k, ""))[:max_width]) for r in rows))) for k in keys}
    header = "  ".join(f"{k:{widths[k]}}" for k in keys)
    print(header)
    print("-" * len(header))
    for r in rows:
        line = "  ".join(f"{str(r.get(k, ''))[:widths[k]]:{widths[k]}}" for k in keys)
        print(line)


def cmd_tables(_args) -> int:
    with _connect() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename"
        )
        tables = [r["tablename"] for r in cur.fetchall()]
        rows = []
        for t in tables:
            cur.execute(f"SELECT count(*) AS n FROM {t}")
            rows.append({"table": t, "rows": cur.fetchone()["n"]})
        _print_rows(rows)
    return 0


def cmd_show(args) -> int:
    with _connect() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(f"SELECT * FROM {args.table} LIMIT %s", (args.limit,))
        _print_rows([dict(r) for r in cur.fetchall()])
    return 0


def cmd_sql(args) -> int:
    with _connect() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(args.sql)
        if cur.description is None:
            conn.commit()
            print(f"OK, rowcount={cur.rowcount}")
        else:
            _print_rows([dict(r) for r in cur.fetchall()])
    return 0


def cmd_eval_report(args) -> int:
    with _connect() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            """
            SELECT backend,
                   COUNT(*) AS n,
                   AVG(retrieval_latency_ms)::INTEGER AS retr_mean_ms,
                   percentile_cont(0.5) WITHIN GROUP
                       (ORDER BY retrieval_latency_ms)::INTEGER AS retr_p50_ms,
                   percentile_cont(0.95) WITHIN GROUP
                       (ORDER BY retrieval_latency_ms)::INTEGER AS retr_p95_ms,
                   AVG(answer_latency_ms)::INTEGER AS ans_mean_ms
            FROM eval_retrieval_runs
            WHERE run_tag = %s
            GROUP BY backend ORDER BY backend
            """,
            (args.run_tag,),
        )
        print(f"=== 延迟 run_tag={args.run_tag} ===")
        _print_rows([dict(r) for r in cur.fetchall()])

        cur.execute(
            """
            SELECT r.backend, s.metric_name,
                   COUNT(s.score) AS n,
                   ROUND(AVG(s.score)::numeric, 3) AS mean,
                   ROUND(percentile_cont(0.5) WITHIN GROUP
                       (ORDER BY s.score)::numeric, 3) AS p50,
                   ROUND(percentile_cont(0.95) WITHIN GROUP
                       (ORDER BY s.score)::numeric, 3) AS p95,
                   SUM(CASE WHEN s.error IS NOT NULL THEN 1 ELSE 0 END) AS errs
            FROM eval_retrieval_runs r
            JOIN eval_metric_scores s ON s.run_id = r.id
            WHERE r.run_tag = %s
            GROUP BY r.backend, s.metric_name
            ORDER BY r.backend, s.metric_name
            """,
            (args.run_tag,),
        )
        print(f"\n=== 指标 run_tag={args.run_tag} ===")
        _print_rows([dict(r) for r in cur.fetchall()])
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("tables", help="列出所有表及行数")

    p_show = sub.add_parser("show", help="查看单表前 N 行")
    p_show.add_argument("table")
    p_show.add_argument("--limit", type=int, default=10)

    p_sql = sub.add_parser("sql", help="执行任意 SQL")
    p_sql.add_argument("sql")

    p_rep = sub.add_parser("eval-report", help="查看某次评测的汇总")
    p_rep.add_argument("--run-tag", required=True)

    args = ap.parse_args()
    handlers = {
        "tables": cmd_tables, "show": cmd_show,
        "sql": cmd_sql, "eval-report": cmd_eval_report,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
