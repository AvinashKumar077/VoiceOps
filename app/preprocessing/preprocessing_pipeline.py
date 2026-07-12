from app.models.conversation import Conversation
from app.preprocessing.review_validator import ReviewValidator
from app.preprocessing.text_cleaner import TextCleaner


class PreprocessingPipeline:
    """
    Coordinates preprocessing steps before reviews
    enter the AI pipeline.
    """

    def __init__(self):
        self.validator = ReviewValidator()
        self.cleaner = TextCleaner()

    def process(
            self,
            conversations: list[Conversation],
    ) -> list[Conversation]:

        processed = []

        for conversation in conversations:

            if not self.validator.is_valid(conversation.text):
                continue

            conversation.text = self.cleaner.clean(
                conversation.text
            )

            processed.append(conversation)

        return processed
