# RAG 模块化拼装重构 — 实施计划

> 来源：`doc/RAG核心模块与模块化拼装分析.md` 第六章
> 范围：6.1（RagBackend 抽象层）+ 6.2.1（并发查询）+ 6.2.2（30s 超时）+ 6.2.3（先传后删）
> 不在本次范围：6.3（最小评估集，需独立标注 50 条历史 query）

---

## Context（为什么做这件事）

工程目前的现实：

1. `forum_client._get_response_data()` 直接耦合 LightRAG HTTP 协议（`/query` + `/query/data` 两次串行 POST，timeout=600s）。文档 6.2 把"卡在 Level 3 Modular RAG 门口"的根因定位到这里：换任何后端都要改业务代码。
2. `src/rag/` 与 `src/rag/adapters/` 目录已存在，但 **`.py` 源文件已被删除**（只剩 `__pycache__/` 内的 `factory.pyc`、`protocol.pyc`、`base_adapter.pyc`、`lightrag_adapter.pyc`）。说明此前曾有 RagBackend 抽象的初稿，需要重建。
3. `src/update_lightrag/increment_date_update_timer.py:185-190` 的增量刷新顺序是 "先 delete 旧文档 → 再 upload 新文档"，存在检索空窗期。

本次目标：**把 forum_client 与 LightRAG 解耦成"接口 + 实现"，并顺手清掉三个零成本痛点**。完成后 forum_client 仅认 `RagBackend` 接口，LightRAG 是其中一个实现；后续接 pgvector / Milvus 不需要动业务代码。

**不变量（铁律）**：`retrieve_documents_for_topic()` 返回值仍然是 `{'topic_id', 'related_docs', 'data'}`，`related_docs` 是字符串（含 ```json 围栏块），`data` 是 dict（含 `chunks` 列表）。下游 `monitor._generate_related_links`、`data_processor.format_search_results_for_prompt`、`ai_processor.call_large_model` 全部不动。

---

## Step 0：批准后立即同步实施计划到工程内

```bash
cp "C:/Users/Administrator/.claude/plans/twinkling-giggling-blum.md" \
   "D:/user/code/forum-reply-robot/doc/RAG模块化重构实施计划.md"
```

让仓库内也有一份可追溯的实施记录（工程文档都在 `doc/` 下）。

---

## Step 1：新建 RagBackend 抽象层

### 1.1 `src/rag/__init__.py`（CREATE）

```python
from .protocol import RagBackend
from .factory import get_rag_backend

__all__ = ["RagBackend", "get_rag_backend"]
```

### 1.2 `src/rag/protocol.py`（CREATE）

`Protocol` + `@runtime_checkable`，3.9/3.11 双版本兼容。

```python
from typing import Protocol, runtime_checkable, TypedDict, Any, Dict

class RagQueryResult(TypedDict, total=False):
    related_docs: str
    data: Dict[str, Any]

@runtime_checkable
class RagBackend(Protocol):
    def query(
        self,
        query: str,
        *,
        top_k: int,
        chunk_top_k: int,
        enable_rerank: bool,
        only_need_context: bool,
        only_need_prompt: bool,
    ) -> RagQueryResult: ...
```

**契约**：`related_docs` 必须是 `str`（可空），`data` 必须是 `dict`（可空）；失败时实现层返回 `{'related_docs': '', 'data': {}}` 而不是抛异常 / 返回 None — 这与 `monitor.py:319-335` 的 graceful fallback 路径对齐。

### 1.3 `src/rag/factory.py`（CREATE）

```python
from typing import Mapping, Any
from .protocol import RagBackend
from .adapters.lightrag_adapter import LightRAGAdapter
from src.ForumBot.logging_config import main_logger as logger

_REGISTRY = {"lightrag": LightRAGAdapter}

def get_rag_backend(config: Mapping[str, Any]) -> RagBackend:
    name = ((config.get("retrieval") or {}).get("backend") or "lightrag").lower()
    cls = _REGISTRY.get(name)
    if cls is None:
        logger.warning(f"未知的 retrieval.backend={name!r}，回退到 lightrag")
        cls = LightRAGAdapter
    return cls(config)
```

未知 backend → warning + 回退到 lightrag（让监控循环不至于因为配置笔误整体挂掉）。

### 1.4 `src/rag/adapters/__init__.py`（CREATE）

```python
from .base_adapter import BaseRagAdapter
from .lightrag_adapter import LightRAGAdapter

__all__ = ["BaseRagAdapter", "LightRAGAdapter"]
```

### 1.5 `src/rag/adapters/base_adapter.py`（CREATE）

```python
from typing import Any, Mapping
from ..protocol import RagQueryResult

class BaseRagAdapter:
    def __init__(self, config: Mapping[str, Any]):
        self.config = config

    @staticmethod
    def _empty_result() -> RagQueryResult:
        return {"related_docs": "", "data": {}}
```

### 1.6 `src/rag/adapters/lightrag_adapter.py`（CREATE）

包当前 LightRAG HTTP，并把 6.2.1 / 6.2.2 一并落地：

```python
from concurrent.futures import ThreadPoolExecutor
import requests
from typing import Any, Mapping
from .base_adapter import BaseRagAdapter
from ..protocol import RagQueryResult
from src.ForumBot.logging_config import main_logger as logger

DEFAULT_TIMEOUT = 30

class LightRAGAdapter(BaseRagAdapter):
    def __init__(self, config: Mapping[str, Any]):
        super().__init__(config)
        retrieval = config.get("retrieval", {}) or {}
        self.base_url = retrieval["base_url"]
        self.endpoint = retrieval["query_endpoint"]
        self.verify_ssl = retrieval.get("verify_ssl", True)
        self.timeout = retrieval.get("timeout", DEFAULT_TIMEOUT)

    def query(self, query, *, top_k, chunk_top_k, enable_rerank,
              only_need_context, only_need_prompt) -> RagQueryResult:
        url = f"{self.base_url}{self.endpoint}"
        url_data = f"{self.base_url}{self.endpoint}/data"
        payload = {
            "query": query,
            "only_need_prompt": only_need_prompt,
            "only_need_context": only_need_context,
            "top_k": top_k,
            "chunk_top_k": chunk_top_k,
            "enable_rerank": enable_rerank,
        }
        try:
            with ThreadPoolExecutor(max_workers=2) as ex:
                f1 = ex.submit(self._post, url, payload)
                f2 = ex.submit(self._post, url_data, payload)
                r1, r2 = f1.result(), f2.result()
            return {"related_docs": (r1 or {}).get("response") or "",
                    "data": r2 or {}}
        except (requests.RequestException, ValueError) as e:
            logger.error(f"LightRAG 请求/解析错误: {e}")
            return self._empty_result()

    def _post(self, url, payload):
        resp = requests.post(url, json=payload, verify=self.verify_ssl, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()
```

ThreadPoolExecutor per-call（最多 2 worker、生命周期 < 30s，开销可忽略；context manager 保证清理）。timeout 默认 30s，可被 `retrieval.timeout` 覆盖（留逃生通道）。

---

## Step 2：改 forum_client 走接口

### `src/ForumBot/forum_client.py`（MODIFY）

只动 3 处，其它方法（`fetch_topic_details`、`reply_to_topic`、`search_related_topics`、`_remove_html_tags`）一字不改。

**a. 顶部 import 增加**：
```python
from src.rag import get_rag_backend
```

**b. `__init__` 改为**：
```python
def __init__(self, config):
    self.config = config
    self.rag_backend = get_rag_backend(config)
```

**c. `retrieve_documents_for_topic` 改为直接调 backend，并删除 `_get_response_data`**：

```python
def retrieve_documents_for_topic(self, topic):
    topic_id = topic['id']
    query = f"{topic['title']} {topic['user_question']}"
    logger.info(f"正在为帖子 {topic_id} 检索相关文档...")

    rcfg = self.config.get('retrieval', {}) or {}
    res = self.rag_backend.query(
        query,
        top_k=rcfg['top_k'],
        chunk_top_k=rcfg['chunk_top_k'],
        enable_rerank=rcfg['enable_rerank'],
        only_need_context=rcfg.get('only_need_context', True),
        only_need_prompt=rcfg.get('only_need_prompt', False),
    )
    related_docs = res.get('related_docs', '') or ''
    data = res.get('data', {}) or {}

    if related_docs:
        logger.info(f"帖子 {topic_id} 检索到相关文档")
    else:
        logger.info(f"帖子 {topic_id} 未检索到相关文档")
    return {'topic_id': topic_id, 'related_docs': related_docs, 'data': data}
```

`_get_response_data` 私有、无外部引用，删除安全。

---

## Step 3：6.2.3 增量更新先传后删

### `src/update_lightrag/increment_date_update_timer.py`（MODIFY）

`update_lightrag_task` 现行顺序（185-190）：

```
delete_document_from_file()  ← 先删
filter.filter_upload_files()
image_processor.process_image_from_files()
upload_all_documents_from_file()  ← 后传
```

调整为：

```python
# 1. 先过滤 + 处理图片（与 RAG 服务无关）
self.filter.filter_upload_files()
self.image_processor.process_image_from_files(self.config['lightrag_paths']['new_rag_files'])

# 2. 上传新文档
self.lightrag_client.upload_all_documents_from_file(
    self.config['lightrag_paths']['new_rag_files'],
    self.config['retrieval']['base_url'])

# 3. 等管道处理完，再删旧文档（避免检索空窗）
self.lightrag_client.wait_for_pipeline_status_not_busy(self.config['retrieval']['base_url'])
if not self.lightrag_client.is_all_file_processed(self.config['retrieval']['base_url']):
    logger.warning("[增量] 新文档未全部 ready，本轮跳过删除旧文档，下次再试")
    return
self.lightrag_client.delete_document_from_file(
    self.config['lightrag_paths']['delete_rag_files_id'],
    self.config['retrieval']['base_url'])
```

`wait_for_pipeline_status_not_busy` 与 `is_all_file_processed` 已在 `lightrag_client.py:252-365` 实现，复用即可，不写新 API。

---

## Step 4：配置加 backend 字段

### `config/config.txt`（MODIFY）

在 `retrieval:` 块顶部加一行：

```yaml
retrieval:
  backend: 'lightrag'        # 新增：lightrag / 未来 pgvector / milvus
  base_url: "https://lightrag-cn4.test.osinfra.cn"
  query_endpoint: "/query"
  # ...原有键全部保留
```

实施时同步检查：`config/config.yaml.startup-bak`、`config/config.yaml.bak` 是否需要同步新增（取决于工程是否有 `config.txt → *.bak` 的生成脚本，没有就手动同步）。**未加这行也不致命**——factory 默认 lightrag。

---

## Step 5：测试改造

### 5.1 `tests/test_forum_client.py`（MODIFY）

`tests/test_forum_client.py:176-211` 两个测试 patch 的是 `src.ForumBot.forum_client.requests.post`。改造后 forum_client 不再直接调 `requests`，patch 路径必须迁移到 adapter：

```python
@patch('src.rag.adapters.lightrag_adapter.requests.post')
def test_retrieve_documents_for_topic_success(self, mock_post, client):
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {'response': 'test response'}
    mock_post.return_value = mock_response
    topic = {'id': 123, 'title': 'Test Title', 'user_question': 'Test Question'}
    result = client.retrieve_documents_for_topic(topic)
    assert result['topic_id'] == 123
    assert result['related_docs'] == 'test response'
    assert isinstance(result['data'], dict)
```

`test_retrieve_documents_for_topic_exception` 的断言 `result['related_docs'] is None` 改为 `== ''`（adapter 异常路径返回空字符串而不是 None — 是修了潜在 unpack bug 而非破坏契约）。

### 5.2 `tests/test_rag_lightrag_adapter.py`（CREATE）

```python
import pytest
from unittest.mock import patch, Mock
from src.rag.adapters.lightrag_adapter import LightRAGAdapter
from src.rag.factory import get_rag_backend

CONFIG = {
    'retrieval': {
        'backend': 'lightrag', 'base_url': 'https://r.test',
        'query_endpoint': '/query', 'verify_ssl': False,
        'top_k': 5, 'chunk_top_k': 5, 'enable_rerank': True,
        'only_need_context': True, 'only_need_prompt': False,
    }
}

@patch('src.rag.adapters.lightrag_adapter.requests.post')
def test_query_combines_two_endpoints(mock_post):
    def side(url, **kw):
        m = Mock(); m.raise_for_status = Mock()
        m.json.return_value = ({'response': 'R'} if url.endswith('/query')
                               else {'chunks': [{'file_path': 'a_123.json'}]})
        return m
    mock_post.side_effect = side
    out = LightRAGAdapter(CONFIG).query('q', top_k=5, chunk_top_k=5,
        enable_rerank=True, only_need_context=True, only_need_prompt=False)
    assert out['related_docs'] == 'R'
    assert out['data']['chunks'][0]['file_path'] == 'a_123.json'

@patch('src.rag.adapters.lightrag_adapter.requests.post', side_effect=Exception('boom'))
def test_query_returns_empty_on_failure(mock_post):
    out = LightRAGAdapter(CONFIG).query('q', top_k=5, chunk_top_k=5,
        enable_rerank=True, only_need_context=True, only_need_prompt=False)
    assert out == {'related_docs': '', 'data': {}}

def test_factory_default_and_unknown():
    assert isinstance(get_rag_backend(CONFIG), LightRAGAdapter)
    cfg2 = {'retrieval': {**CONFIG['retrieval'], 'backend': 'no_such'}}
    assert isinstance(get_rag_backend(cfg2), LightRAGAdapter)
```

`tests/conftest.py` 不需要改（不引入新依赖）。

---

## 验证

### 自动化

```bash
pytest tests/test_rag_lightrag_adapter.py -v
pytest tests/test_forum_client.py -v
pytest tests/test_lightrag_client.py -v   # 索引侧回归
pytest tests/ -x                          # 全量
```

### 端到端手动验证

```powershell
# 0. 恢复配置（config.yaml 启动后会被删除，参考 AGENTS.md）
Copy-Item config/config.yaml.startup-bak config/config.yaml

# 1. 启动
$env:PYTHONPATH="."; $env:PYTHONIOENCODING="utf-8"
.venv/Scripts/python.exe main.py

# 2. 健康检查
Invoke-RestMethod http://localhost:5000/health

# 3. 在 logs/main.log 中确认看到下面这一序列：
#    "正在为帖子 <id> 检索相关文档..."
#    "帖子 <id> 检索到相关文档" 或 "帖子 <id> 未检索到相关文档"
#    若 LightRAG 慢，应 ≤30s 触发降级到 search_results 而非 600s 卡死。
```

### 不变量自检

`retrieve_documents_for_topic` 返回值：
- `set(result.keys()) == {'topic_id', 'related_docs', 'data'}`
- `isinstance(result['related_docs'], str)`
- `isinstance(result['data'], dict)`

下游消费者全部能继续工作：
- `monitor.py:319` `'related_docs' not in retrieval_result` → key 始终存在 ✓
- `monitor.py:146` `retrieval_data.get('data', '').get('chunks', '')` → `data` 是 dict，`.get('chunks', '')` 正常 ✓
- `data_processor.format_search_results_for_prompt` 内 `extract_json_blocks(str)` ✓
- `ai_processor.call_large_model(retrieval_result['related_docs'], ...)` → 接收 str ✓

---

## 风险与对策

| # | 风险 | 对策 |
|---|---|---|
| R1 | timeout 600 → 30 后部分长尾请求被切断 | 上游 `monitor.py:319-335` 已有 fallback；`retrieval.timeout` 配置项可临时调高（无需改业务代码） |
| R2 | `tests/test_forum_client.py` 旧 patch 路径失效 → 测试静默发真 HTTP | Build agent 必须 grep `forum_client.requests` 确认无遗漏 |
| R3 | `config.yaml.startup-bak` 与 `config.txt` 不同步 | 实施时检查是否有生成脚本，没有就两边都加 `backend: 'lightrag'` |
| R4 | 6.2.3 先传后删调整后，新文档处理慢导致 `wait_for_pipeline_status_not_busy` 长阻塞 | 函数本身有日志，便于观察；如发现卡死可加 `max_wait` 参数（本次不做） |
| R5 | 配置缺 `retrieval.base_url` → adapter `__init__` 抛 `KeyError` 让 ForumClient 启动失败 | 这是 fail-fast，比静默 600s 等待好；fixture 已含此键 |

---

## 不在本次范围

- **6.3 最小评估集**：需要标注 50 条历史 query 的期望 topic_id，写离线脚本算 Recall@10 / MRR@10。这是一次性投入，做完之后才有"换 pgvector 是好是坏"的量化判据。建议作为下一个独立 PR。
- **后续接 pgvector / Milvus**：本次只做 LightRAG adapter；新增后端只需在 `src/rag/adapters/` 下加文件并在 `factory._REGISTRY` 注册一行。

---

## 实施顺序（建议）

1. Step 0 拷贝 plan 到 `doc/`
2. Step 1.1–1.6 新建 `src/rag/` 全部文件（无外部依赖，先跑通 import）
3. Step 5.2 写 adapter 测试，跑通 → 证明抽象层独立可用
4. Step 2 改 forum_client → 跑 Step 5.1 测试 → 证明业务层接通
5. Step 4 加 config 字段
6. Step 3 改增量更新顺序 → 单跑 `tests/` 全量
7. Step 4 验证 → 端到端手动跑 main.py
