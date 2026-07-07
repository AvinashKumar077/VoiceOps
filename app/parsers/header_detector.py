from dataclasses import dataclass


@dataclass
class HeaderMapping:
    id_column: str | None = None
    text_column: str | None = None
    rating_column: str | None = None
    date_column: str | None = None


class HeaderDetector:
    TEXT_HEADERS = [
        "content",
        "review",
        "comment",
        "feedback",
        "message",
        "text",
        "description",
    ]

    ID_HEADERS = [
        "reviewid",
        "id",
    ]

    RATING_HEADERS = [
        "score",
        "rating",
        "stars",
    ]

    DATE_HEADERS = [
        "at",
        "date",
        "created_at",
        "createdon",
    ]

    def detect(self, headers: list[str]) -> HeaderMapping:

        mapping = HeaderMapping()

        normalized_headers = {
            header.lower().strip(): header
            for header in headers
        }

        for candidate in self.ID_HEADERS:
            if candidate in normalized_headers:
                mapping.id_column = normalized_headers[candidate]
                break

        for candidate in self.TEXT_HEADERS:
            if candidate in normalized_headers:
                mapping.text_column = normalized_headers[candidate]
                break

        for candidate in self.RATING_HEADERS:
            if candidate in normalized_headers:
                mapping.rating_column = normalized_headers[candidate]
                break

        for candidate in self.DATE_HEADERS:
            if candidate in normalized_headers:
                mapping.date_column = normalized_headers[candidate]
                break

        return mapping
