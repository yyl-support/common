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
