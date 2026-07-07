from abc import ABC, abstractmethod

from app.ai.models import (
    LLMRequest,
    LLMResponse,
)


class LLMProvider(ABC):

    @abstractmethod
    def generate(
            self,
            request: LLMRequest,
    ) -> LLMResponse:
        pass