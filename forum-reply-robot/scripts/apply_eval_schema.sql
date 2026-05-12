-- RAG 检索质量离线评测所用的表结构
-- 幂等:全部 IF NOT EXISTS,可重复执行

CREATE TABLE IF NOT EXISTS eval_query_set (
    id              SERIAL PRIMARY KEY,
    query_id        TEXT UNIQUE NOT NULL,
    question        TEXT NOT NULL,
    expected_output TEXT,
    note            TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eval_retrieval_runs (
    id                    SERIAL PRIMARY KEY,
    query_id              TEXT NOT NULL REFERENCES eval_query_set(query_id),
    backend               TEXT NOT NULL,
    run_tag               TEXT NOT NULL,
    retrieval_context     TEXT NOT NULL,
    retrieval_chunks      JSONB,
    actual_output         TEXT,
    retrieval_latency_ms  INTEGER,
    answer_latency_ms     INTEGER,
    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (query_id, backend, run_tag)
);

CREATE INDEX IF NOT EXISTS idx_eval_runs_backend_tag
    ON eval_retrieval_runs (backend, run_tag);

CREATE TABLE IF NOT EXISTS eval_metric_scores (
    id             SERIAL PRIMARY KEY,
    run_id         INTEGER NOT NULL REFERENCES eval_retrieval_runs(id) ON DELETE CASCADE,
    metric_name    TEXT NOT NULL,
    score          REAL,
    threshold      REAL,
    is_successful  BOOLEAN,
    reason         TEXT,
    judge_model    TEXT,
    error          TEXT,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (run_id, metric_name)
);
