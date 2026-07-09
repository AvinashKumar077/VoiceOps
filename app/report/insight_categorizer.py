from app.insights.models import ClusterInsight
from app.report.models import CategorizedInsights

CRITICAL_SEVERITIES = {"critical", "high"}


class InsightCategorizer:
    """Buckets insights using their existing severity/sentiment metadata.

    No LLM call: every ClusterInsight already carries the fields needed
    to decide where it belongs, so categorization is a pure rule engine.

    Sentiment decides *what kind* of insight this is (positive feedback vs.
    a problem); severity only matters once we already know it's a negative
    one, to decide how urgent that problem is. Using severity first would
    let a "High severity" positive cluster (e.g. a beloved core feature)
    land under critical_issues, which is wrong.
    """

    def categorize(
            self,
            insights: list[ClusterInsight],
    ) -> CategorizedInsights:

        critical_issues = []
        positive_feedback = []
        feature_requests = []

        for insight in insights:
            sentiment = insight.sentiment.strip().lower()
            severity = insight.severity.strip().lower()

            if sentiment == "positive":
                positive_feedback.append(insight)
            elif sentiment == "negative" and severity in CRITICAL_SEVERITIES:
                critical_issues.append(insight)
            else:
                feature_requests.append(insight)

        return CategorizedInsights(
            critical_issues=critical_issues,
            feature_requests=feature_requests,
            positive_feedback=positive_feedback,
        )
