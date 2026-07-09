from pydantic import BaseModel

from app.analytics.models import DatasetStatistics
from app.insights.models import ClusterInsight


class ExecutiveSummary(BaseModel):
    overall_sentiment: str
    customer_health: str
    biggest_risk: str
    biggest_opportunity: str
    summary: str


class CategorizedInsights(BaseModel):
    critical_issues: list[ClusterInsight]
    feature_requests: list[ClusterInsight]
    positive_feedback: list[ClusterInsight]


class ProductAnalysisReport(BaseModel):
    executive_summary: ExecutiveSummary
    critical_issues: list[ClusterInsight]
    feature_requests: list[ClusterInsight]
    positive_feedback: list[ClusterInsight]
    statistics: DatasetStatistics
