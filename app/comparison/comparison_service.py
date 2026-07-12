from app.comparison.fingerprint_builder import FingerprintBuilder
from app.comparison.insight_matcher import InsightMatcher
from app.comparison.models import TrendReport
from app.comparison.trend_detector import TrendDetector
from app.report.models import ProductAnalysisReport


class ComparisonService:
    """Compares two ProductAnalysisReports into a TrendReport.

    No LLM call: everything here is derived directly from the two
    reports' own insights via embeddings and arithmetic.
    """

    def __init__(self):
        self.fingerprint_builder = FingerprintBuilder()
        self.matcher = InsightMatcher()
        self.trend_detector = TrendDetector()

    def compare(
            self,
            previous_report: ProductAnalysisReport,
            current_report: ProductAnalysisReport,
    ) -> TrendReport:

        previous_fingerprints = self.fingerprint_builder.build(
            previous_report
        )
        current_fingerprints = self.fingerprint_builder.build(
            current_report
        )

        match_result = self.matcher.match(
            previous_fingerprints,
            current_fingerprints,
        )

        growing_issues, shrinking_issues = self.trend_detector.detect(
            match_result.matched
        )

        return TrendReport(
            new_issues=[
                fp.insight
                for fp in match_result.new_fingerprints
            ],
            resolved_issues=[
                fp.insight
                for fp in match_result.resolved_fingerprints
            ],
            growing_issues=growing_issues,
            shrinking_issues=shrinking_issues,
        )
