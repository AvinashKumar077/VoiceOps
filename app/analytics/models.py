from pydantic import BaseModel


class DatasetStatistics(BaseModel):
    total_reviews: int
    average_rating: float | None
    average_review_length: float
    min_review_length: int
    max_review_length: int
    rating_distribution: dict[int, int]