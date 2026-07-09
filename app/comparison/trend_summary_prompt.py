from app.comparison.models import TrendReport


class TrendSummaryPromptBuilder:

    def build(self, trend_report: TrendReport) -> str:
        return f"""
You are a Senior Product Manager preparing a release comparison summary.
Below are the issue trends between two review periods.

New Issues (present now, absent before)
{self._render_insights(trend_report.new_issues)}

Resolved Issues (present before, absent now)
{self._render_insights(trend_report.resolved_issues)}

Growing Issues (getting worse)
{self._render_trends(trend_report.growing_issues)}

Shrinking Issues (getting better)
{self._render_trends(trend_report.shrinking_issues)}

In 3-5 sentences, summarize what changed between the two periods and
whether the product is trending better or worse overall. Return ONLY
the summary text, no JSON, no code fences, no headers.
"""

    @staticmethod
    def _render_insights(insights) -> str:
        if not insights:
            return "None"

        return "\n".join(
            f"- {insight.title} ({insight.affected_reviews} users)"
            for insight in insights
        )

    @staticmethod
    def _render_trends(trends) -> str:
        if not trends:
            return "None"

        return "\n".join(
            f"- {trend.title}: {trend.previous_reviews} -> "
            f"{trend.current_reviews} users ({trend.change_percent:+.1f}%)"
            for trend in trends
        )
