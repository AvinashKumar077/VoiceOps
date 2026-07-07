class ReviewValidator:
    MIN_TEXT_LENGTH = 2

    def is_valid(self, text: str) -> bool:

        if text is None:
            return False

        text = str(text).strip()

        if not text:
            return False

        if len(text) < self.MIN_TEXT_LENGTH:
            return False

        return True
