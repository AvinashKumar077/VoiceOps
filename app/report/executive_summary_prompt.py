from app.analytics.models import DatasetStatistics
from app.insights.models import ClusterInsight


class ExecutiveSummaryPromptBuilder:

    def build(
            self,
            insights: list[ClusterInsight],
            statistics: DatasetStatistics,
    ) -> str:
        insights_text = "\n----------------\n".join(
            self._render_insight(insight)
            for insight in insights
        )

        statistics_text = self._render_statistics(statistics)

        return f"""
You are a Senior Product Manager.
Below is the overall dataset statistics, followed by the most important
customer insights already extracted from customer reviews. Use both to
judge overall product health: a large volume of critical issues does not
by itself mean poor health if positive sentiment and ratings dominate the
dataset overall.

Dataset Statistics
{statistics_text}

Customer Insights
{insights_text}

Return ONLY valid JSON, no code fences, no commentary:
{{
"overall_sentiment":"",
"customer_health":"",
"biggest_risk":"",
"biggest_opportunity":"",
"summary":""
}}
"""

    @staticmethod
    def _render_statistics(statistics: DatasetStatistics) -> str:
        rating_distribution = ", ".join(
            f"{stars}★: {count}"
            for stars, count in sorted(statistics.rating_distribution.items())
        )

        return f"""Total reviews: {statistics.total_reviews}
Average rating: {statistics.average_rating}
Rating distribution: {rating_distribution}"""

    @staticmethod
    def _render_insight(insight: ClusterInsight) -> str:
        return f"""{insight.title}
Sentiment: {insight.sentiment}
Severity: {insight.severity}
Affected Users: {insight.affected_reviews}
Summary: {insight.summary}"""
