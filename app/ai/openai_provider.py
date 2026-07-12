import os

from dotenv import load_dotenv
from openai import OpenAI

from app.ai.llm_provider import LLMProvider
from app.ai.models import (
    LLMRequest,
    LLMResponse,
)

load_dotenv()


class OpenAIProvider(LLMProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.model = os.getenv(
            "LLM_MODEL",
            "gpt-4.1-mini",
        )

    def generate(
            self,
            request: LLMRequest,
    ) -> LLMResponse:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": request.prompt,
                }
            ],
            temperature=0,
        )

        return LLMResponse(
            content=response.choices[0].message.content
        )