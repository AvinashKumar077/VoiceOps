import re


class TextCleaner:

    def clean(self, text: str) -> str:
        """
        Standardize review text without removing useful information.
        """

        if text is None:
            return ""

        # Convert to string
        text = str(text)

        # Lowercase
        text = text.lower()

        # Replace newlines and tabs with spaces
        text = re.sub(r"[\n\r\t]+", " ", text)

        # Collapse multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Trim
        return text.strip()