import os

from app.ai.gemini_provider import GeminiProvider
from app.ai.llm_provider import LLMProvider
from app.ai.openai_provider import OpenAIProvider


class LLMFactory:

    @staticmethod
    def create() -> LLMProvider:
        provider = os.getenv(
            "LLM_PROVIDER",
            "openai",
        )

        if provider == "openai":
            return OpenAIProvider()

        if provider == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )