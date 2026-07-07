import os

from dotenv import load_dotenv
from google import genai

from app.ai.llm_provider import LLMProvider
from app.ai.models import (
    LLMRequest,
    LLMResponse,
)

load_dotenv()


class GeminiProvider(LLMProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
        self.model = os.getenv(
            "LLM_MODEL",
            "gemini-2.5-flash",
        )

    def generate(
            self,
            request: LLMRequest,
    ) -> LLMResponse:
        response = self.client.models.generate_content(
            model=self.model,
            contents=request.prompt,
        )

        return LLMResponse(
            content=response.text
        )