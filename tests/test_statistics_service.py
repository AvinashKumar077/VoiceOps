from app.analytics.statistics_service import StatisticsService
from app.models.conversation import Conversation


def test_generate_statistics():

    conversations = [
        Conversation(
            id="1",
            text="payment failed",
            source="csv",
            rating=1,
        ),
        Conversation(
            id="2",
            text="great app",
            source="csv",
            rating=5,
        ),
        Conversation(
            id="3",
            text="good service",
            source="csv",
            rating=4,
        ),
    ]

    stats = StatisticsService().generate(conversations)

    assert stats.total_reviews == 3
    assert stats.average_rating == 3.33
    assert stats.rating_distribution[1] == 1
    assert stats.rating_distribution[5] == 1