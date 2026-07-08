import json

from app.ai.factory import LLMFactory
from app.ai.models import LLMRequest
from app.clustering.models import ReviewCluster
from app.insights.batch_prompt_builder import BatchPromptBuilder
from app.insights.models import ClusterInsight


class BatchInsightService:

    def __init__(self):
        self.provider = LLMFactory.create()
        self.builder = BatchPromptBuilder()

    def analyze(
            self,
            clusters: list[ReviewCluster],
    ) -> list[ClusterInsight]:
        if not clusters:
            return []

        prompt = self.builder.build(clusters)

        response = self.provider.generate(
            LLMRequest(
                prompt=prompt
            )
        )

        raw_insights = json.loads(
            self._strip_code_fence(response.content)
        )

        clusters_by_id = {
            cluster.cluster_id: cluster
            for cluster in clusters
        }

        insights = []

        for raw_insight in raw_insights:
            insight = ClusterInsight.model_validate(raw_insight)

            cluster = clusters_by_id.get(insight.cluster_id)
            if cluster is None:
                continue

            # Enrich the AI response with our own metadata
            insight.affected_reviews = cluster.size
            insight.confidence = cluster.average_similarity
            insight.sample_reviews = cluster.representative_reviews

            insights.append(insight)

        return insights

    @staticmethod
    def _strip_code_fence(content: str) -> str:
        content = content.strip()

        if content.startswith("```"):
            content = content.strip("`")
            content = content.removeprefix("json").strip()

        return content
