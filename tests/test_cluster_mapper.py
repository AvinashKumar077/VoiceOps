from app.clustering.cluster_mapper import ClusterMapper
from app.models.conversation import Conversation


def test_mapper():

    conversations = [

        Conversation(
            id="1",
            text="Payment failed",
            source="csv"
        ),

        Conversation(
            id="2",
            text="Unable to pay",
            source="csv"
        ),

        Conversation(
            id="3",
            text="Weather is nice",
            source="csv"
        ),

    ]

    labels = [0, 0, 1]

    result = ClusterMapper().map(
        conversations,
        labels,
    )

    assert len(result) == 2

    assert result[0].size == 2