from pydantic import BaseModel


class ClusterInsight(BaseModel):
    title: str
    summary: str
    sentiment: str
    severity: str
    business_impact: str
    engineering_effort: str
    recommended_priority: str