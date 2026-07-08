from pydantic import BaseModel

from app.analytics.models import DatasetStatistics
from app.insights.models import ClusterInsight


class AnalysisReport(BaseModel):
    statistics: DatasetStatistics
    insights: list[ClusterInsight]