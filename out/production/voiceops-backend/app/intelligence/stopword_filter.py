from app.intelligence.constants import STOPWORDS


class StopwordFilter:

    def filter(self, tokens: list[str]) -> list[str]:
        return [
            token
            for token in tokens
            if token not in STOPWORDS
        ]
