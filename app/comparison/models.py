from pydantic import BaseModel

from app.insights.models import ClusterInsight


class IssueFingerprint(BaseModel):
    """Normalized representation of an insight used for comparison.

    Keeps the comparison engine independent of presentation fields
    (summary, sample_reviews, ...) so enriching ClusterInsight later
    doesn't require touching matching/trend logic.
    """

    model_config = {"arbitrary_types_allowed": True}

    title: str
    embedding: list[float]
    affected_reviews: int
    insight: ClusterInsight


class Trend(BaseModel):
    title: str
    previous_reviews: int
    current_reviews: int
    change_percent: float
    direction: str


class TrendReport(BaseModel):
    new_issues: list[ClusterInsight]
    resolved_issues: list[ClusterInsight]
    growing_issues: list[Trend]
    shrinking_issues: list[Trend]
    executive_trend_summary: str = ""
