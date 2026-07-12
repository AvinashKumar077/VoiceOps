from pydantic import BaseModel


class ReviewCluster(BaseModel):
    cluster_id: int
    size: int
    representative_reviews: list[str]
    average_similarity: float
