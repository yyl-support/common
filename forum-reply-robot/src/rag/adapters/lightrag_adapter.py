from concurrent.futures import ThreadPoolExecutor
from typing import Any, Mapping

import requests

from src.ForumBot.logging_config import main_logger as logger
from ..protocol import RagQueryResult
from .base_adapter import BaseRagAdapter

DEFAULT_TIMEOUT = 300


class LightRAGAdapter(BaseRagAdapter):
    def __init__(self, config: Mapping[str, Any]):
        super().__init__(config)
        retrieval = config.get("retrieval", {}) or {}
        self.base_url = retrieval["base_url"]
        self.endpoint = retrieval["query_endpoint"]
        self.verify_ssl = retrieval.get("verify_ssl", True)
        self.timeout = retrieval.get("timeout", DEFAULT_TIMEOUT)

    def query(
        self,
        query: str,
        *,
        top_k: int,
        chunk_top_k: int,
        enable_rerank: bool,
        only_need_context: bool,
        only_need_prompt: bool,
    ) -> RagQueryResult:
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
            return {
                "related_docs": (r1 or {}).get("response") or "",
                "data": r2 or {},
            }
        except requests.RequestException as e:
            logger.error(f"LightRAG 请求错误: {e}")
            return self._empty_result()
        except ValueError as e:
            logger.error(f"LightRAG JSON 解析错误: {e}")
            return self._empty_result()
        except Exception as e:
            logger.error(f"LightRAG 未预期错误: {e}")
            return self._empty_result()

    def _post(self, url: str, payload: dict) -> dict:
        resp = requests.post(
            url, json=payload, verify=self.verify_ssl, timeout=self.timeout
        )
        resp.raise_for_status()
        return resp.json()
