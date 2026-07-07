import pandas as pd

from app.parsers.conversation_mapper import ConversationMapper
from app.parsers.header_detector import HeaderMapping


def test_map_google_play_review():

    row = pd.Series({
        "reviewId": "123",
        "content": "Payment failed",
        "score": 1,
        "at": "2024-01-01"
    })

    mapping = HeaderMapping(
        id_column="reviewId",
        text_column="content",
        rating_column="score",
        date_column="at"
    )

    conversation = ConversationMapper().map(
        row,
        mapping
    )

    assert conversation.id == "123"
    assert conversation.text == "Payment failed"
    assert conversation.rating == 1