"""评测用的 DB 访问封装。所有评测脚本都走这里,不要在别处直接开连接。"""
from __future__ import annotations

import json
from contextlib import contextmanager
from typing import Any, Iterable, Mapping, Optional

import psycopg2
from psycopg2.extras import Json, RealDictCursor


def get_db_params(config: Mapping[str, Any]) -> dict:
    db = config.get("database", {}) or {}
    return {
        "host": db["host"],
        "port": db["port"],
        "database": db["database"],
        "user": db["user"],
        "password": db["password"],
        "sslmode": db.get("sslmode", "disable"),
    }


@contextmanager
def connect(config: Mapping[str, Any]):
    conn = psycopg2.connect(**get_db_params(config))
    try:
        yield conn
    finally:
        conn.close()


def load_query_set(conn) -> list[dict]:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "SELECT query_id, question, expected_output, note "
            "FROM eval_query_set ORDER BY query_id"
        )
        return [dict(r) for r in cur.fetchall()]


def insert_retrieval_run(
    conn,
    *,
    query_id: str,
    backend: str,
    run_tag: str,
    retrieval_context: str,
    retrieval_chunks: Iterable[str],
    actual_output: Optional[str],
    retrieval_latency_ms: Optional[int],
    answer_latency_ms: Optional[int],
) -> int:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO eval_retrieval_runs (
                query_id, backend, run_tag,
                retrieval_context, retrieval_chunks,
                actual_output, retrieval_latency_ms, answer_latency_ms
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (query_id, backend, run_tag) DO UPDATE SET
                retrieval_context = EXCLUDED.retrieval_context,
                retrieval_chunks  = EXCLUDED.retrieval_chunks,
                actual_output     = EXCLUDED.actual_output,
                retrieval_latency_ms = EXCLUDED.retrieval_latency_ms,
                answer_latency_ms    = EXCLUDED.answer_latency_ms,
                created_at = CURRENT_TIMESTAMP
            RETURNING id
            """,
            (
                query_id, backend, run_tag,
                retrieval_context, Json(list(retrieval_chunks)),
                actual_output, retrieval_latency_ms, answer_latency_ms,
            ),
        )
        run_id = cur.fetchone()[0]
    conn.commit()
    return run_id


def insert_metric_score(
    conn,
    *,
    run_id: int,
    metric_name: str,
    score: Optional[float],
    threshold: Optional[float],
    is_successful: Optional[bool],
    reason: Optional[str],
    judge_model: Optional[str],
    error: Optional[str] = None,
) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO eval_metric_scores (
                run_id, metric_name, score, threshold,
                is_successful, reason, judge_model, error
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (run_id, metric_name) DO UPDATE SET
                score = EXCLUDED.score,
                threshold = EXCLUDED.threshold,
                is_successful = EXCLUDED.is_successful,
                reason = EXCLUDED.reason,
                judge_model = EXCLUDED.judge_model,
                error = EXCLUDED.error,
                created_at = CURRENT_TIMESTAMP
            """,
            (run_id, metric_name, score, threshold,
             is_successful, reason, judge_model, error),
        )
    conn.commit()


def summarize_run_tag(conn, run_tag: str) -> list[dict]:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            """
            SELECT r.backend, s.metric_name,
                   COUNT(s.score) AS n,
                   AVG(s.score)::REAL AS mean,
                   percentile_cont(0.5) WITHIN GROUP (ORDER BY s.score)::REAL AS p50,
                   percentile_cont(0.95) WITHIN GROUP (ORDER BY s.score)::REAL AS p95,
                   SUM(CASE WHEN s.error IS NOT NULL THEN 1 ELSE 0 END) AS errors
            FROM eval_retrieval_runs r
            JOIN eval_metric_scores s ON s.run_id = r.id
            WHERE r.run_tag = %s
            GROUP BY r.backend, s.metric_name
            ORDER BY r.backend, s.metric_name
            """,
            (run_tag,),
        )
        return [dict(r) for r in cur.fetchall()]


def summarize_latency(conn, run_tag: str) -> list[dict]:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            """
            SELECT backend,
                   COUNT(*) AS n,
                   AVG(retrieval_latency_ms)::INTEGER AS retrieval_mean_ms,
                   percentile_cont(0.5) WITHIN GROUP
                       (ORDER BY retrieval_latency_ms)::INTEGER AS retrieval_p50_ms,
                   percentile_cont(0.95) WITHIN GROUP
                       (ORDER BY retrieval_latency_ms)::INTEGER AS retrieval_p95_ms,
                   AVG(answer_latency_ms)::INTEGER AS answer_mean_ms
            FROM eval_retrieval_runs
            WHERE run_tag = %s
            GROUP BY backend
            ORDER BY backend
            """,
            (run_tag,),
        )
        return [dict(r) for r in cur.fetchall()]
