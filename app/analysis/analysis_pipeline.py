from app.analytics.statistics_service import StatisticsService
from app.clustering.cluster_service import ClusterService
from app.embeddings.embedding_service import EmbeddingService
from app.insights.insight_pipeline import InsightPipeline
from app.models.conversation import Conversation
from app.report.models import ProductAnalysisReport
from app.report.report_pipeline import ReportPipeline


class AnalysisPipeline:

    def __init__(self):

        self.statistics_service = StatisticsService()
        self.embedding_service = EmbeddingService()
        self.cluster_service = ClusterService()
        self.insight_pipeline = InsightPipeline()
        self.report_pipeline = ReportPipeline()

    def analyze(
            self,
            conversations: list[Conversation],
    ) -> ProductAnalysisReport:

        statistics = self.statistics_service.generate(
            conversations
        )

        texts = [
            conversation.text
            for conversation in conversations
        ]

        embeddings = self.embedding_service.embed_batch(
            texts
        )

        clusters = self.cluster_service.cluster(
            conversations,
            embeddings,
        )

        insights = self.insight_pipeline.generate(
            clusters
        )

        return self.report_pipeline.build(
            statistics=statistics,
            insights=insights,
        )