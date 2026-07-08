from pydantic import BaseModel, Field


class ClusterInsight(BaseModel):
    cluster_id: int
    title: str
    summary: str
    sentiment: str
    severity: str
    business_impact: str
    engineering_effort: str
    recommended_priority: str

    affected_reviews: int = 0
    confidence: float = 0.0
    sample_reviews: list[str] = Field(default_factory=list)