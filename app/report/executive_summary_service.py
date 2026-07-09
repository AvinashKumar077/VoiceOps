from app.ai.factory import LLMFactory
from app.ai.json_utils import parse_json
from app.ai.models import LLMRequest
from app.analytics.models import DatasetStatistics
from app.insights.models import ClusterInsight
from app.report.executive_summary_prompt import ExecutiveSummaryPromptBuilder
from app.report.models import ExecutiveSummary


class ExecutiveSummaryService:

    def __init__(self):
        self.provider = LLMFactory.create()
        self.builder = ExecutiveSummaryPromptBuilder()

    def generate(
            self,
            insights: list[ClusterInsight],
            statistics: DatasetStatistics,
    ) -> ExecutiveSummary:
        if not insights:
            return ExecutiveSummary(
                overall_sentiment="Unknown",
                customer_health="Unknown",
                biggest_risk="No insights available",
                biggest_opportunity="No insights available",
                summary="Not enough data was gathered to produce an executive summary.",
            )

        prompt = self.builder.build(insights, statistics)

        response = self.provider.generate(
            LLMRequest(
                prompt=prompt
            )
        )

        raw_summary = parse_json(response.content)

        return ExecutiveSummary.model_validate(raw_summary)
