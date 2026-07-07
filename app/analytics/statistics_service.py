from collections import Counter

from app.analytics.models import DatasetStatistics
from app.models.conversation import Conversation


class StatisticsService:

    def generate(
            self,
            conversations: list[Conversation],
    ) -> DatasetStatistics:
        total_reviews = len(conversations)

        ratings = [
            c.rating
            for c in conversations
            if c.rating is not None
        ]

        lengths = [
            len(c.text.split())
            for c in conversations
        ]

        distribution = Counter(ratings)

        average_rating = (
            round(sum(ratings) / len(ratings), 2)
            if ratings
            else None
        )

        average_length = (
            round(sum(lengths) / len(lengths), 2)
            if lengths
            else 0
        )

        return DatasetStatistics(
            total_reviews=total_reviews,
            average_rating=average_rating,
            average_review_length=average_length,
            min_review_length=min(lengths) if lengths else 0,
            max_review_length=max(lengths) if lengths else 0,
            rating_distribution=dict(distribution),
        )
