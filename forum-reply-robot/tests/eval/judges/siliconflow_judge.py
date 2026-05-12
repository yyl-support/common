"""SiliconFlow 评测裁判 LLM 适配器。

deepeval 的 BaseLLM 要求同步 generate 和异步 a_generate。SiliconFlow 暴露 OpenAI 兼容
的 /v1/chat/completions,直接用 openai 客户端即可。评测时 temperature=0 保证可复现。
"""
from __future__ import annotations

from typing import Any, Mapping
import asyncio

from openai import OpenAI
from deepeval.models.base_model import DeepEvalBaseLLM


class SiliconFlowJudge(DeepEvalBaseLLM):
    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
        model: str,
        temperature: float = 0.0,
        timeout: int = 120,
    ):
        self._base_url = base_url
        self._api_key = api_key
        self._model = model
        self._temperature = temperature
        self._timeout = timeout
        self._client: OpenAI | None = None

    def load_model(self):
        if self._client is None:
            self._client = OpenAI(
                base_url=self._base_url,
                api_key=self._api_key,
                timeout=self._timeout,
            )
        return self._client

    def generate(self, prompt: str, schema: Any = None) -> Any:
        client = self.load_model()
        kwargs: dict[str, Any] = {
            "model": self._model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self._temperature,
        }
        if schema is not None:
            kwargs["response_format"] = {"type": "json_object"}
        resp = client.chat.completions.create(**kwargs)
        text = resp.choices[0].message.content or ""
        if schema is not None:
            import json as _json
            return schema.model_validate(_json.loads(text))
        return text

    async def a_generate(self, prompt: str, schema: Any = None) -> Any:
        return await asyncio.to_thread(self.generate, prompt, schema)

    def get_model_name(self) -> str:
        return self._model


def build_judge_from_config(config: Mapping[str, Any]) -> SiliconFlowJudge:
    api = config.get("api", {}) or {}
    eval_cfg = (config.get("eval", {}) or {})
    return SiliconFlowJudge(
        base_url=api["base_url"],
        api_key=api["api_key"],
        model=eval_cfg.get("judge_model") or api.get("model_name"),
        temperature=float(eval_cfg.get("judge_temperature", 0.0)),
        timeout=int(eval_cfg.get("judge_timeout", 120)),
    )
