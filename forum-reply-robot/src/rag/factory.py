from typing import Mapping, Any
from .protocol import RagBackend
from .adapters.lightrag_adapter import LightRAGAdapter
from src.ForumBot.logging_config import main_logger as logger

_REGISTRY = {
    "lightrag": LightRAGAdapter,
}


def get_rag_backend(config: Mapping[str, Any]) -> RagBackend:
    name = ((config.get("retrieval") or {}).get("backend") or "lightrag").lower()
    cls = _REGISTRY.get(name)
    if cls is None:
        logger.warning(f"未知的 retrieval.backend={name!r}，回退到 lightrag")
        cls = LightRAGAdapter
    return cls(config)
