import re


class Tokenizer:

    def tokenize(self, text: str) -> list[str]:
        if not text:
            return []

        return re.findall(r"[a-zA-Z']+", text.lower())
