import json

from app.ai.factory import LLMFactory
from app.ai.models import LLMRequest
from app.clustering.models import ReviewCluster
from app.insights.models import ClusterInsight
from app.insights.prompt_builder import PromptBuilder


class InsightService:

    def __init__(self):
        self.provider = LLMFactory.create()
        self.builder = PromptBuilder()

    def analyze(
            self,
            cluster: ReviewCluster,
    ) -> ClusterInsight:
        prompt = self.builder.build(
            cluster.size,
            cluster.representative_reviews,
        )

        response = self.provider.generate(
            LLMRequest(
                prompt=prompt
            )
        )

        return ClusterInsight.model_validate(
            json.loads(
                self._strip_code_fence(response.content)
            )
        )

    @staticmethod
    def _strip_code_fence(content: str) -> str:
        content = content.strip()

        if content.startswith("```"):
            content = content.strip("`")
            content = content.removeprefix("json").strip()

        return content