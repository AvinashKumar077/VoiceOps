from app.clustering.models import ReviewCluster
from app.insights.batch_insight_service import BatchInsightService
from app.insights.constants import (
    CLUSTER_SIMILARITY_WEIGHT,
    CLUSTER_SIZE_WEIGHT,
    MAX_CLUSTERS_PER_BATCH,
    MIN_CLUSTER_SIZE,
    PRIORITY_ORDER,
)
from app.insights.models import ClusterInsight


class InsightPipeline:

    def __init__(self):
        self.service = BatchInsightService()

    def generate(
            self,
            clusters: list[ReviewCluster],
    ) -> list[ClusterInsight]:

        candidates = [
            cluster
            for cluster in clusters
            if cluster.size >= MIN_CLUSTER_SIZE
        ]

        top_clusters = sorted(
            candidates,
            key=self._score,
            reverse=True,
        )[:MAX_CLUSTERS_PER_BATCH]

        insights = self.service.analyze(top_clusters)

        return sorted(
            insights,
            key=lambda insight: (
                PRIORITY_ORDER.get(
                    insight.recommended_priority,
                    99,
                ),
                -insight.affected_reviews,
            ),
        )

    @staticmethod
    def _score(cluster: ReviewCluster) -> float:
        return (
            cluster.size * CLUSTER_SIZE_WEIGHT
            + cluster.average_similarity * 100 * CLUSTER_SIMILARITY_WEIGHT
        )
