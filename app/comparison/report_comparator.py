from app.comparison.comparison_service import ComparisonService
from app.comparison.models import TrendReport
from app.comparison.trend_summary_service import TrendSummaryService
from app.report.models import ProductAnalysisReport


class ReportComparator:

    def __init__(self):
        self.comparison_service = ComparisonService()
        self.trend_summary_service = TrendSummaryService()

    def compare(
            self,
            previous_report: ProductAnalysisReport,
            current_report: ProductAnalysisReport,
    ) -> TrendReport:

        trend_report = self.comparison_service.compare(
            previous_report,
            current_report,
        )

        trend_report.executive_trend_summary = (
            self.trend_summary_service.generate(trend_report)
        )

        return trend_report
