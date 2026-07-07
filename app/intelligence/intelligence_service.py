from app.intelligence.frequency_analyzer import FrequencyAnalyzer
from app.intelligence.models import (
    IntelligenceSummary,
    KeywordFrequency,
    PhraseFrequency,
)
from app.intelligence.ngram_extractor import NGramExtractor
from app.intelligence.stopword_filter import StopwordFilter
from app.intelligence.tokenizer import Tokenizer
from app.models.conversation import Conversation


class IntelligenceService:

    def __init__(self):
        self.tokenizer = Tokenizer()
        self.stopword_filter = StopwordFilter()
        self.ngram_extractor = NGramExtractor()
        self.frequency_analyzer = FrequencyAnalyzer()

    def analyze(
            self,
            conversations: list[Conversation],
    ) -> IntelligenceSummary:

        all_tokens = []
        all_phrases = []

        for conversation in conversations:

            tokens = self.tokenizer.tokenize(conversation.text)

            tokens = self.stopword_filter.filter(tokens)

            all_tokens.extend(tokens)

            # Generate bigrams
            phrases = self.ngram_extractor.extract(tokens, n=2)
            all_phrases.extend(phrases)

        keyword_frequency = self.frequency_analyzer.analyze(
            all_tokens,
            top_n=20,
        )

        phrase_frequency = self.frequency_analyzer.analyze(
            all_phrases,
            top_n=20,
        )

        return IntelligenceSummary(
            top_keywords=[
                KeywordFrequency(
                    keyword=word,
                    count=count,
                )
                for word, count in keyword_frequency
            ],
            top_phrases=[
                PhraseFrequency(
                    phrase=phrase,
                    count=count,
                )
                for phrase, count in phrase_frequency
            ],
        )