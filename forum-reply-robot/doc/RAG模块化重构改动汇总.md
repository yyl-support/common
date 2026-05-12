# RAG 模块化拼装重构 — 改动汇总

> 完成日期：2026-05-08
> 关联文档：`doc/RAG核心模块与模块化拼装分析.md`、`doc/RAG模块化重构实施计划.md`

---

## 新增（6 个文件）

| 文件 | 作用 |
| --- | --- |
| `src/rag/__init__.py` | 命名空间暴露：`RagBackend`、`RagQueryResult`、`get_rag_backend` |
| `src/rag/protocol.py` | `RagBackend` Protocol + `RagQueryResult` TypedDict，定义统一接口契约 |
| `src/rag/factory.py` | `get_rag_backend(config)` 按 `retrieval.backend` 选择实现，未知值回退 lightrag |
| `src/rag/adapters/__init__.py` | adapters 子包暴露 |
| `src/rag/adapters/base_adapter.py` | 轻量基类，提供 `_empty_result()` 工具方法 |
| `src/rag/adapters/lightrag_adapter.py` | LightRAG 适配器：`ThreadPoolExecutor` 并发 `/query` + `/query/data`、timeout 30s、失败返回空 dict |
| `tests/test_rag_lightrag_adapter.py` | adapter 单测：双端点合并、失败降级、工厂默认/未知/缺省 |
| `doc/RAG模块化重构实施计划.md` | 与 plan 文件同步的实施记录 |

## 修改（5 个文件）

| 文件 | 改动要点 |
| --- | --- |
| `src/ForumBot/forum_client.py` | `__init__` 注入 `self.rag_backend = get_rag_backend(config)`；`retrieve_documents_for_topic` 改为走 backend；**删除 `_get_response_data`** |
| `src/update_lightrag/increment_date_update_timer.py` | `update_lightrag_task` 顺序改为：过滤 → 处理图片 → 上传新文档 → `wait_for_pipeline_status_not_busy` + `is_all_file_processed` 校验 → 删旧文档（消除检索空窗） |
| `config/config.txt`、`config/config.yaml.startup-bak`、`config/config.yaml.bak` | `retrieval:` 块新增 `backend: 'lightrag'` |
| `tests/test_forum_client.py` | patch 路径迁移到 `src.rag.adapters.lightrag_adapter.requests.post`；新增 `test_retrieve_documents_uses_rag_backend` 验证接口接通；异常断言由 `is None` 改为 `== ''` |
| `tests/test_forum_client_pre_audit.py` | 测试 config 补 `retrieval` 节（fail-fast 副作用：缺 base_url 会让 ForumClient 实例化失败） |

---

## 落地的 doc 6.x 项

| 项 | 状态 | 实现位置 |
| --- | --- | --- |
| 6.1 RagBackend 抽象层 | ✓ | `src/rag/protocol.py`、`src/rag/factory.py`、`src/rag/adapters/lightrag_adapter.py` |
| 6.2.1 `/query` + `/query/data` 并发 | ✓ | `lightrag_adapter.LightRAGAdapter.query` 内 `ThreadPoolExecutor(max_workers=2)` per-call |
| 6.2.2 timeout 600→30s 降级 | ✓ | `lightrag_adapter.DEFAULT_TIMEOUT = 30`；`retrieval.timeout` 可覆盖；上游 `monitor.py:319-335` 已有 fallback |
| 6.2.3 增量更新先传后删 | ✓ | `increment_date_update_timer.update_lightrag_task` 顺序调整 + 管道状态校验 |
| 6.3 最小评估集（50 条 query） | ✗ | 不在本次范围，需独立 PR |

---

## 测试结果

| 套件 | 结果 |
| --- | --- |
| `tests/test_rag_lightrag_adapter.py` | **5/5 通过**（双端点合并、失败降级、工厂默认/未知/缺省） |
| `tests/test_forum_client.py` | **12/12 通过**（含新增的 `test_retrieve_documents_uses_rag_backend`） |
| 全量 `tests/` | **217 通过 / 1 失败** |

唯一失败：`tests/test_monitor_pre_audit.py::test_sync_csv_to_git_repo_runs_validated_git_commands` — 与本次改造**无关**，在改动前的 baseline 下也失败（git 路径校验逻辑与测试 mock 不对齐的历史问题）。

### Smoke check

```python
from src.rag import get_rag_backend, RagBackend
from src.ForumBot.forum_client import ForumClient

cfg = {'retrieval': {'backend': 'lightrag', 'base_url': 'https://r.test',
                     'query_endpoint': '/query', 'top_k': 5, 'chunk_top_k': 5,
                     'enable_rerank': True}}
be = get_rag_backend(cfg)
assert type(be).__name__ == 'LightRAGAdapter'
assert isinstance(be, RagBackend)

fc = ForumClient(cfg)
assert type(fc.rag_backend).__name__ == 'LightRAGAdapter'
assert not hasattr(fc, '_get_response_data')   # 已删除
```

全部通过。

---

## 数据契约不变量（重构前后保持）

`retrieve_documents_for_topic()` 返回值始终是 `{'topic_id', 'related_docs', 'data'}`：

- `related_docs` 是 `str`（含 ```json 围栏块），可空
- `data` 是 `dict`（含 `chunks` 列表），可空
- 失败路径返回空字符串 + 空 dict，**不再返回 None**（修复了原 `_get_response_data` 异常路径返回单 `None` 的潜在 unpack bug）

下游消费者全部不受影响：

| 调用点 | 访问方式 | 校验 |
| --- | --- | --- |
| `monitor.py:319` | `'related_docs' not in retrieval_result` | key 始终存在 ✓ |
| `monitor.py:146` | `retrieval_data.get('data', '').get('chunks', '')` | `data` 是 dict，链式访问正常 ✓ |
| `data_processor.format_search_results_for_prompt` | `extract_json_blocks(related_docs)` | 接收 str ✓ |
| `ai_processor.call_large_model` | `(retrieval_result['related_docs'], ...)` | 接收 str ✓ |

---

## 后续可做（不在本次）

- 6.3 最小评估集：标注 50 条历史 query 的期望 topic_id，写离线脚本算 Recall@10 / MRR@10，作为后续后端切换的量化基线
- 接 pgvector / Milvus：在 `src/rag/adapters/` 下加文件，`factory._REGISTRY` 注册一行；业务代码无需改动
