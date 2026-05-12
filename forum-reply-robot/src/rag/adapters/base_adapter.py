from typing import Any, Mapping
from ..protocol import RagQueryResult


class BaseRagAdapter:
    def __init__(self, config: Mapping[str, Any]):
        self.config = config

    @staticmethod
    def _empty_result() -> RagQueryResult:
        return {"related_docs": "", "data": {}}
