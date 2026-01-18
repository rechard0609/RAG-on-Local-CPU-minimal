from __future__ import annotations

import requests

from .base import BaseLLM, LLMResult
from settings import API_KEYS


class SolarLLM(BaseLLM):
    name = "solar"

    def __init__(
        self,
        model: str,
        base_url: str = "https://api.upstage.ai/v1",
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = (
            API_KEYS.get("solar", {})
            .get("api_key", "")
            .strip()
        )

    def generate(
        self,
        prompt: str,
        max_tokens: int = 512,
        temperature: float = 0.2,
    ) -> LLMResult:
        if not self.api_key:
            raise RuntimeError("UPSTAGE_API_KEY is not set")

        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": float(temperature),
            "max_tokens": int(max_tokens),
        }

        r = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60,
        )
        if r.status_code >= 400:
            raise RuntimeError(
                f"Upstage API error {r.status_code}: {r.text}"
            )

        data = r.json()
        text = data["choices"][0]["message"]["content"]
        usage = data.get("usage") or {}

        return LLMResult(
            text=text,
            usage={
                "prompt_tokens": int(
                    usage.get("prompt_tokens", 0)
                ),
                "completion_tokens": int(
                    usage.get("completion_tokens", 0)
                ),
                "total_tokens": int(
                    usage.get("total_tokens", 0)
                ),
            },
        )
