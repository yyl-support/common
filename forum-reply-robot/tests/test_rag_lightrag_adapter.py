from unittest.mock import patch, Mock

from src.rag.adapters.lightrag_adapter import LightRAGAdapter
from src.rag.factory import get_rag_backend


CONFIG = {
    "retrieval": {
        "backend": "lightrag",
        "base_url": "https://r.test",
        "query_endpoint": "/query",
        "verify_ssl": False,
        "top_k": 5,
        "chunk_top_k": 5,
        "enable_rerank": True,
        "only_need_context": True,
        "only_need_prompt": False,
    }
}


@patch("src.rag.adapters.lightrag_adapter.requests.post")
def test_query_combines_two_endpoints(mock_post):
    def side(url, **kwargs):
        m = Mock()
        m.raise_for_status = Mock()
        if url.endswith("/query"):
            m.json.return_value = {"response": "R"}
        else:
            m.json.return_value = {"chunks": [{"file_path": "a_123.json"}]}
        return m

    mock_post.side_effect = side

    out = LightRAGAdapter(CONFIG).query(
        "q",
        top_k=5,
        chunk_top_k=5,
        enable_rerank=True,
        only_need_context=True,
        only_need_prompt=False,
    )
    assert out["related_docs"] == "R"
    assert out["data"]["chunks"][0]["file_path"] == "a_123.json"


@patch(
    "src.rag.adapters.lightrag_adapter.requests.post",
    side_effect=Exception("boom"),
)
def test_query_returns_empty_on_failure(mock_post):
    out = LightRAGAdapter(CONFIG).query(
        "q",
        top_k=5,
        chunk_top_k=5,
        enable_rerank=True,
        only_need_context=True,
        only_need_prompt=False,
    )
    assert out == {"related_docs": "", "data": {}}


def test_factory_default_returns_lightrag():
    assert isinstance(get_rag_backend(CONFIG), LightRAGAdapter)


def test_factory_unknown_backend_falls_back():
    cfg = {"retrieval": {**CONFIG["retrieval"], "backend": "no_such"}}
    assert isinstance(get_rag_backend(cfg), LightRAGAdapter)


def test_factory_missing_backend_key_defaults_to_lightrag():
    cfg = {"retrieval": {**CONFIG["retrieval"]}}
    cfg["retrieval"].pop("backend", None)
    assert isinstance(get_rag_backend(cfg), LightRAGAdapter)
