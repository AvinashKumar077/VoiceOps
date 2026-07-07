from app.models.conversation import Conversation
from app.preprocessing.preprocessing_pipeline import PreprocessingPipeline


def test_pipeline():

    conversations = [
        Conversation(
            id="1",
            text=" PAYMENT FAILED ",
            source="csv"
        ),
        Conversation(
            id="2",
            text="",
            source="csv"
        ),
        Conversation(
            id="3",
            text="Payment     Failed",
            source="csv"
        )
    ]

    pipeline = PreprocessingPipeline()

    result = pipeline.process(conversations)

    assert len(result) == 2

    assert result[0].text == "payment failed"

    assert result[1].text == "payment failed"