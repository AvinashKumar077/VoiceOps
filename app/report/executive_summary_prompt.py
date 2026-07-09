from app.insights.models import ClusterInsight


class ExecutiveSummaryPromptBuilder:

    def build(
            self,
            insights: list[ClusterInsight],
    ) -> str:
        insights_text = "\n----------------\n".join(
            self._render_insight(insight)
            for insight in insights
        )

        return f"""
You are a Senior Product Manager.
Below are the most important customer insights, already extracted from
customer reviews. Summarize the overall health of the product.

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
    def _render_insight(insight: ClusterInsight) -> str:
        return f"""{insight.title}
Sentiment: {insight.sentiment}
Severity: {insight.severity}
Affected Users: {insight.affected_reviews}
Summary: {insight.summary}"""
