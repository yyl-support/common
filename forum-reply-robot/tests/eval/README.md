# RAG 检索质量离线评测(Phase 1)

## 作用

在"同一 LLM + 同一 prompt"的前提下,对不同 RAG 后端(当前 `lightrag`,未来 `pgvector` 等)跑同一批 query,产出 4 个 deepeval 指标 + 检索延迟,全部落 PostgreSQL。

## 指标

| 指标 | 测什么 | 需要 GT |
|---|---|:-:|
| Faithfulness | 答案是否只基于上下文,是否存在矛盾 | 否 |
| Contextual Relevancy | 检索片段本身是否贴题 | 否 |
| Contextual Precision | 相关片段是否排在前面 | **是** |
| Contextual Recall | 检索是否覆盖答案所需事实 | **是** |

Phase 1 的 query 集里 `expected_output` 允许为空;为空时 Precision/Recall 自动 skipped,不阻塞。

## 数据库

依赖 3 张表(在 `scripts/apply_eval_schema.sql`):
- `eval_query_set` — 评测用 query + 可选 GT
- `eval_retrieval_runs` — 每条 (query, backend, run_tag) 的检索/答案/延迟
- `eval_metric_scores` — 每个 (run, metric) 的分数与理由

连接配置从 `config/config.yaml` 读(脚本会在找不到时回退到 `.local-bak` / `.startup-bak`)。

## 前置

1. 本地已有 PostgreSQL,已创建 `openeuler_forumrobot` 库
2. 已应用 schema:
   ```bash
   .venv/Scripts/python.exe -c "import psycopg2,sys; \
     conn=psycopg2.connect(host='127.0.0.1',port=5432,user='postgres',password='gorden',database='openeuler_forumrobot'); \
     conn.cursor().execute(open('scripts/apply_eval_schema.sql').read()); conn.commit()"
   ```
3. 已安装 deepeval:
   ```bash
   .venv/Scripts/python.exe -m pip install deepeval
   ```

## 插入 query 集

编辑 `scripts/insert_eval_queries.sql.tpl` 后,用 DB 客户端执行,或:

```bash
.venv/Scripts/python.exe scripts/db_shell.py sql "$(cat scripts/insert_eval_queries.sql.tpl)"
```

## 运行

```bash
# 只跑检索链路 + 写库,不调 judge(最省 token,验链路用)
.venv/Scripts/python.exe tests/eval/run_eval.py --run-tag smoke --dry-run

# 完整评测
.venv/Scripts/python.exe tests/eval/run_eval.py --run-tag baseline-2026-05-11

# 只跑前 3 条
.venv/Scripts/python.exe tests/eval/run_eval.py --run-tag debug --limit 3
```

## 查报表

```bash
.venv/Scripts/python.exe scripts/db_shell.py eval-report --run-tag baseline-2026-05-11
```

## 换后端

`config.yaml` 里改 `retrieval.backend`(lightrag 或未来的 pgvector),重跑时指定新的 `--run-tag`,同一份 query 集的两次结果就能在 DB 里直接 join 对比。

## Phase 2 待办

- 为 8~10 条 query 人工标 `expected_output`,启用 Precision / Recall
- 实现 pgvector adapter 并注册到 `src/rag/factory.py`
- 加一份 CI 回归脚本:检测指标回归就失败
