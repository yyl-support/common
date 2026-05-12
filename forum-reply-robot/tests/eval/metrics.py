"""4 个 deepeval 指标的组装。

关键约束:
- Precision / Recall 需要 expected_output(GT);若 GT 为空,本函数返回 skipped 结果,
  不抛异常。
- 所有指标共用同一个 judge LLM 实例,避免重复初始化。
- include_reason=True 让 judge 产出判分理由,方便离线排查(尤其是失败 case)。
"""
from __future__ import annotations

from typing import Any, Optional

from deepeval.metrics import (
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric,
    FaithfulnessMetric,
)
from deepeval.test_case import LLMTestCase


_METRIC_PLAN = [
    ("faithfulness", FaithfulnessMetric, False),
    ("contextual_relevancy", ContextualRelevancyMetric, False),
    ("contextual_precision", ContextualPrecisionMetric, True),
    ("contextual_recall", ContextualRecallMetric, True),
]


def build_test_case(
    *,
    question: str,
    answer: str,
    chunks: list[str],
    expected_output: Optional[str],
) -> LLMTestCase:
    return LLMTestCase(
        input=question,
        actual_output=answer or "",
        retrieval_context=chunks or [""],
        expected_output=expected_output,
    )


def run_all_metrics(
    tc: LLMTestCase,
    *,
    judge_llm: Any,
    threshold: float = 0.5,
) -> list[dict]:
    results: list[dict] = []
    judge_name = getattr(judge_llm, "get_model_name", lambda: "unknown")()
    for name, cls, needs_gt in _METRIC_PLAN:
        base = {
            "metric_name": name,
            "threshold": threshold,
            "judge_model": judge_name,
        }
        if needs_gt and not tc.expected_output:
            results.append({
                **base,
                "score": None, "is_successful": None, "reason": None,
                "error": "skipped: expected_output missing",
            })
            continue
        metric = cls(threshold=threshold, model=judge_llm, include_reason=True)
        try:
            metric.measure(tc)
            results.append({
                **base,
                "score": float(metric.score) if metric.score is not None else None,
                "is_successful": bool(metric.is_successful()),
                "reason": getattr(metric, "reason", None),
                "error": None,
            })
        except Exception as exc:  # noqa: BLE001
            results.append({
                **base,
                "score": None, "is_successful": None, "reason": None,
                "error": f"{type(exc).__name__}: {exc}",
            })
    return results
