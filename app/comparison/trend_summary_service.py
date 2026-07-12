from app.ai.factory import LLMFactory
from app.ai.json_utils import strip_code_fence
from app.ai.models import LLMRequest
from app.comparison.models import TrendReport
from app.comparison.trend_summary_prompt import TrendSummaryPromptBuilder


class TrendSummaryService:

    def __init__(self):
        self.provider = LLMFactory.create()
        self.builder = TrendSummaryPromptBuilder()

    def generate(self, trend_report: TrendReport) -> str:
        has_changes = (
            trend_report.new_issues
            or trend_report.resolved_issues
            or trend_report.growing_issues
            or trend_report.shrinking_issues
        )

        if not has_changes:
            return "No meaningful change detected between the two periods."

        prompt = self.builder.build(trend_report)

        response = self.provider.generate(
            LLMRequest(
                prompt=prompt
            )
        )

        return strip_code_fence(response.content)
