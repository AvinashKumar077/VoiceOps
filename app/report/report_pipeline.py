from app.analytics.models import DatasetStatistics
from app.insights.models import ClusterInsight
from app.report.executive_summary_service import ExecutiveSummaryService
from app.report.insight_categorizer import InsightCategorizer
from app.report.models import ProductAnalysisReport


class ReportPipeline:

    def __init__(self):
        self.categorizer = InsightCategorizer()
        self.executive_summary_service = ExecutiveSummaryService()

    def build(
            self,
            statistics: DatasetStatistics,
            insights: list[ClusterInsight],
    ) -> ProductAnalysisReport:

        categorized = self.categorizer.categorize(insights)

        executive_summary = self.executive_summary_service.generate(
            insights,
            statistics,
        )

        return ProductAnalysisReport(
            executive_summary=executive_summary,
            critical_issues=categorized.critical_issues,
            feature_requests=categorized.feature_requests,
            positive_feedback=categorized.positive_feedback,
            statistics=statistics,
        )
