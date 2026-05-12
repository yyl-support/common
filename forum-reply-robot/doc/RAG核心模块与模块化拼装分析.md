# RAG 核心模块与模块化拼装分析

> 输出日期：2026-05-08
> 范围：结合《工程部署启动流程.md》与《RAG优化建议.md》，梳理 RAG 技术的核心模块、主流"模块化拼装"方案的形态，并对照本工程（forum-reply-robot）当前的实现状态给出定位与改进方向。

---

## 一、RAG 的核心模块

RAG（Retrieval-Augmented Generation）按数据流向可以拆成四大块，主流框架（LangChain、LlamaIndex、Haystack、RAGFlow、LightRAG、Dify 等）都是围绕这张拼图做的封装与扩展。

### 1.1 索引侧（离线构建知识库）

| 模块 | 作用 | 典型实现 |
| --- | --- | --- |
| Loader / 多源接入 | 把 PDF、HTML、Markdown、数据库等接进流水线 | Unstructured、LlamaHub Readers |
| Chunking 切分 | 将长文档切成可检索单元 | 固定长度、语义切分、结构化切分、Parent-Child |
| Embedding 向量化 | 将文本转为向量 | bge-m3、Qwen-Embedding、text-embedding-3 |
| VectorStore 存储 | 持久化并索引向量 | Milvus、Qdrant、**pgvector**、Elasticsearch |
| Graph Index（可选） | 抽实体关系构建知识图谱 | LightRAG、GraphRAG、Neo4j |

### 1.2 检索侧（在线查询）

| 模块 | 作用 | 典型实现 |
| --- | --- | --- |
| Query Rewriting | 改写 / 扩展用户查询 | HyDE、Step-back、Multi-Query |
| Retrieval 召回 | 稠密向量 / BM25 / 图谱检索 | 对应各后端 API |
| Hybrid Fusion | 多路召回融合 | RRF、加权融合 |
| Reranker 重排 | Cross-Encoder 精排 | bge-reranker、Qwen3-Reranker |
| Context Compression | 上下文压缩与去重 | LLMLingua、摘要式压缩 |

### 1.3 生成侧

- Prompt 组装与上下文裁剪
- LLM 生成（可加 Function Call / Tool Use）
- 引用溯源（Citation）
- 幻觉检测与答案质量校验

### 1.4 评估与编排

- **评估**：RAGAS、TruLens、DeepEval（答案相关性、忠实度、上下文精/召回率）
- **编排**：LangGraph、Haystack Pipeline、Dify 工作流——把上述模块串成 DAG

---

## 二、成熟方案 = 模块拼装

当前工业界的共识就是 **"可插拔组件 + 可编排流程"**。下面是几种主流拼装模式：

| 模式 | 组合 | 适用场景 |
| --- | --- | --- |
| Naive RAG | Chunk → Embed → VectorSearch → LLM | PoC / 小规模 |
| **Advanced RAG** | + Query Rewrite + Hybrid + Rerank + 多闸门生成 | 生产级 FAQ / 文档问答 |
| GraphRAG | + 知识图谱检索融合 | 多跳推理、跨文档 |
| Contextual Retrieval | Chunk 预生成上下文摘要再嵌入 | 召回率要求高 |
| Agentic RAG | LLM 自主决定检索策略（Self-RAG / CRAG） | 复杂任务、多工具协同 |

选型要看三件事：**数据形态**（文本 / 结构化 / 图）、**查询复杂度**（事实问答 / 多跳推理）、**延迟与成本预算**。没有银弹，拼装才是常态。

---

## 三、本工程的 RAG 模块映射

把 forum-reply-robot 按上述四大块拆开看：

### 3.1 索引侧

| 标准模块 | 工程现状 | 代码位置 |
| --- | --- | --- |
| Loader | ForumDataFetcher（Discourse JSON）+ GitCodeFullFetcher / IncrementFetcher（GitCode Markdown） | `src/update_lightrag/forum_data_Fetcher.py`、`gitode_full_fetcher.py`、`gitcode_api_increment_fetcher.py` |
| 多模态预处理 | ImageProcessor 调 Qwen3-VL 把帖子图片转文本描述 | `update_lightrag/image_processor.py` |
| 内容过滤 | Filter 按关键词剔除敏感文件 | `update_lightrag/filter.py` |
| Chunking + Embedding + Graph + VectorStore | **全部封装在 LightRAG 远端服务内部**，工程侧只保留 `POST /documents/upload` | `lightrag_client.py` |
| 增量调度 | UpdateLightRAGTimer（每日 UTC 18:00） | `increment_date_update_timer.py` |

### 3.2 检索侧

| 标准模块 | 工程现状 |
| --- | --- |
| Query Rewriting | **缺失**，只用 `"{title} {user_question}"` 拼串 |
| 向量 + KG 召回 | LightRAG `POST /query` + `POST /query/data`（串行两次） |
| BM25 / 全文召回 | doc-search.openeuler.org（外部站内搜索） |
| Hybrid Fusion | **没有显式融合**，两路结果在 `format_search_results_for_prompt()` 里简单拼接进 prompt |
| Rerank | LightRAG 内部 `enable_rerank=true`，工程层无法干预 |

### 3.3 生成侧

这是工程里做得最细的一层，已经是**多闸门 Pipeline**：

```
check_prompt_injection
      ↓
summarize_text
      ↓
search_related_topics（外部搜索）
      ↓
retrieve_documents_for_topic（LightRAG）
      ↓
format_search_results_for_prompt
      ↓
call_large_model
      ↓
check_answer_relevance
      ↓
check_answer_quality
      ↓
summarize_answer
      ↓
reply_to_topic
```

每一步都是独立的 LLM 调用，可以单独替换、关停或加旁路，是比较标准的"LLM 作为组件"的拼装思路。

### 3.4 评估与编排

| 维度 | 现状 |
| --- | --- |
| 编排 | `monitor.py` 手写 `while True` 循环，没用 LangGraph / Dify 工作流引擎，但直观可读 |
| 离线评估 | **完全缺失**：无回归集、无 RAGAS、无 LLM-as-judge |
| 可观测性 | Token 追踪有（`consume_tokens_topic` 表），检索质量的端到端监控没有 |

---

## 四、本工程在 RAG 成熟度阶梯上的位置

```
Level 1  Naive RAG        : Loader → Chunk → Embed → VectorSearch → LLM
Level 2  Advanced RAG     : + Hybrid + Rerank + 多闸门生成              ← 工程当前位置
Level 3  Modular RAG      : 适配层解耦 + 可插拔后端 + 评估闭环
Level 4  Agentic RAG      : LLM 自主决定检索策略（Self-RAG / CRAG）
```

本工程已具备 Level 2 的多数元素（混合检索、rerank、生成侧多闸门），但**卡在 Level 3 门口**，原因有二：

1. **后端被锁死**：切块、embedding、KG、向量检索、rerank 全塞进 LightRAG，换任一层都要换整个服务。
2. **没有适配层**：`forum_client.retrieve_documents_for_topic()` 直接耦合到 LightRAG HTTP 协议，所以"想换 pgvector"等于"改业务代码"。`src/rag/adapters/` 目录已预留但尚未填充。

---

## 五、"可拼装"的三大关键标志

判断一个 RAG 方案是否真正做到了模块化拼装，看三点：

### 5.1 后端抽象层

定义统一接口，业务只认接口不认实现：

```python
class RagBackend(Protocol):
    def upsert(self, docs: list[Document]) -> None: ...
    def delete(self, ids: list[str]) -> None: ...
    def query(self, text: str, top_k: int, filters: dict) -> list[Hit]: ...
```

LightRAG / pgvector / Milvus / ES 都是实现类，配置一切：

```yaml
retrieval:
  backend: pgvector   # 或 lightrag / milvus
```

### 5.2 流水线可编排

LangGraph、Haystack Pipeline、Dify DAG 把每个模块（Retriever、Reranker、Compressor、Generator）做成节点，边上挂配置。本工程 `_process_new_topics()` 其实就是手写的 DAG，只是还没抽象出来。

### 5.3 评估闭环可插拔

RAGAS / TruLens 能单独挂到任一节点上打分，无需改检索或生成代码。本工程目前最缺这一层——没有它就无法量化"换了 pgvector 后召回是更好还是更差"。

---

## 六、给本工程的下一步建议

按 `RAG优化建议.md` 中 Step 1 的思路，**优先做后端抽象层**（投入小、收益大），具体三件事：

### 6.1 引入 `RagBackend` 接口（阻塞项）

- 在 `src/rag/adapters/` 下定义 `RagBackend` 抽象类
- 实现 `LightRAGAdapter`（包一层现状，零业务改动）
- 把 `forum_client.retrieve_documents_for_topic()` 改为走接口
- 配置项 `retrieval.backend` 支持 `lightrag` / `pgvector` 在线切换

### 6.2 立刻可做的小修（零成本高收益）

源自《RAG优化建议》第五章，不需要等重构：

- `_get_response_data()` 里 `/query` 和 `/query/data` 串行双调用 → 改并发
- `timeout=600s` → 降到 30s，超时立即降级到外部搜索结果
- 增量更新"先删后传"的空窗期 → 改为"先传新版 → 校验 → 再删旧版"

### 6.3 补一个最小评估集（先验证，再重构）

- 挑 50 条线上历史 query，标注期望命中的 topic_id
- 写一个离线脚本：跑一遍当前后端，输出 Recall@10 / MRR@10
- 后续任何后端替换都以这个评估集为准绳

完成以上三步后，工程会从"隐式拼装 + 黑盒后端"升级到"**显式拼装 + 可换后端 + 有评估基线**"，这正是成熟 RAG 方案的核心形态，也是迈向 Level 3 Modular RAG 的入场券。

---

## 七、一句话总结

> 当前主流 RAG 方案都是 **"可插拔模块 + 可编排流程 + 可插拔评估"** 的三段式拼装。本工程已经在生成侧做到了很好的多闸门拼装，但在索引/检索侧被 LightRAG 封成了黑盒。下一步的关键动作不是急着换后端，而是先**建抽象层 + 建评估集**——有了这两块地基，无论后续选 pgvector、Milvus 还是保留 LightRAG，都能以低风险、可量化的方式演进。
