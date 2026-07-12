from app.comparison.models import IssueFingerprint
from app.embeddings.embedding_service import EmbeddingService
from app.insights.models import ClusterInsight
from app.report.models import ProductAnalysisReport


class FingerprintBuilder:

    def __init__(self):
        self.embedding_service = EmbeddingService()

    def build(
            self,
            report: ProductAnalysisReport,
    ) -> list[IssueFingerprint]:

        insights = self._all_insights(report)

        return [
            self._to_fingerprint(insight)
            for insight in insights
        ]

    @staticmethod
    def _all_insights(
            report: ProductAnalysisReport,
    ) -> list[ClusterInsight]:
        return (
            report.critical_issues
            + report.feature_requests
            + report.positive_feedback
        )

    def _to_fingerprint(
            self,
            insight: ClusterInsight,
    ) -> IssueFingerprint:
        text = f"{insight.title}. {insight.summary}"

        embedding = self.embedding_service.embed(text)

        return IssueFingerprint(
            title=insight.title,
            embedding=embedding,
            affected_reviews=insight.affected_reviews,
            insight=insight,
        )
