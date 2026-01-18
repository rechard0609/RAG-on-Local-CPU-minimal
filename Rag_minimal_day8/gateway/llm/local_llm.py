from __future__ import annotations

import requests

from .base import BaseLLM, LLMResult


class LocalLLM(BaseLLM):
    """
    Local CPU LLM adapter.

    This class acts as a thin HTTP adapter to a running llama.cpp server.
    No API key is required.

    Expected server:
    - llama.cpp with --server enabled
    - Classic endpoint: POST /completion

    Example endpoint:
    - http://local-llm:8080
    """

    name = "local"

    def __init__(self, endpoint: str):
        # e.g. http://local-llm:8080
        self.endpoint = endpoint.rstrip("/")

    def generate(
        self,
        prompt: str,
        max_tokens: int = 512,
        temperature: float = 0.2,
    ) -> LLMResult:
        url = f"{self.endpoint}/completion"
        payload = {
            "prompt": prompt,
            "n_predict": int(max_tokens),
            "temperature": float(temperature),
        }

        r = requests.post(
            url,
            json=payload,
            timeout=60,
        )
        if r.status_code >= 400:
            raise RuntimeError(
                f"Local LLM error {r.status_code}: {r.text}\n"
                f"Hint: ensure llama.cpp server is running "
                f"and supports POST /completion"
            )

        data = r.json()

        # Known response shapes:
        # 1) {"content": "..."}
        # 2) {"completion": "..."}
        text = (
            data.get("content")
            or data.get("completion")
            or ""
        )

        return LLMResult(
            text=text,
            usage=None,  # llama.cpp does not expose token usage
        )
