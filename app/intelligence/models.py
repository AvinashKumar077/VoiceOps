from pydantic import BaseModel


class KeywordFrequency(BaseModel):
    keyword: str
    count: int


class PhraseFrequency(BaseModel):
    phrase: str
    count: int


class IntelligenceSummary(BaseModel):
    top_keywords: list[KeywordFrequency]
    top_phrases: list[PhraseFrequency]