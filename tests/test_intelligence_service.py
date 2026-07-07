from app.intelligence.intelligence_service import IntelligenceService
from app.models.conversation import Conversation


def test_analyze_keywords():

    conversations = [
        Conversation(
            id="1",
            text="Payment failed",
            source="csv",
        ),
        Conversation(
            id="2",
            text="Payment failed again",
            source="csv",
        ),
        Conversation(
            id="3",
            text="Refund issued",
            source="csv",
        ),
    ]

    result = IntelligenceService().analyze(conversations)

    assert result.top_keywords[0].keyword == "payment"
    assert result.top_keywords[0].count == 2