from __future__ import annotations

import requests

from .base import BaseLLM, LLMResult
from settings import API_KEYS  # ← 수정!


class GeminiLLM(BaseLLM):
    name = "gemini"

    def __init__(self, model: str):
        self.model = model
        self.api_key = (
            API_KEYS.get("gemini", {})
            .get("api_key", "")
            .strip()
        )

    def generate(
        self,
        prompt: str,
        max_tokens: int = 512,
        temperature: float = 0.2
    ) -> LLMResult:
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is not set")

        url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            f"models/{self.model}:generateContent"
        )
        params = {"key": self.api_key}
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ],
            "generationConfig": {
                "maxOutputTokens": int(max_tokens),
                "temperature": float(temperature),
            },
        }

        resp = requests.post(
            url,
            params=params,
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()

        text = ""
        try:
            text = (
                data["candidates"][0]
                ["content"]["parts"][0]["text"]
            )
        except Exception:
            text = str(data)

        # Gemini usage fields may vary
        usage = None
        meta = data.get("usageMetadata") or {}
        if meta:
            usage = {
                "prompt_tokens": int(
                    meta.get("promptTokenCount", 0)
                ),
                "completion_tokens": int(
                    meta.get("candidatesTokenCount", 0)
                ),
                "total_tokens": int(
                    meta.get("totalTokenCount", 0)
                ),
            }

        return LLMResult(
            text=text,
            usage=usage,
        )
