from app.intelligence.ngram_extractor import NGramExtractor


def test_bigram():

    extractor = NGramExtractor()

    result = extractor.extract(
        ["payment", "failed", "today"],
        n=2,
    )

    assert result == [
        "payment failed",
        "failed today",
    ]


def test_trigram():

    extractor = NGramExtractor()

    result = extractor.extract(
        ["payment", "failed", "today"],
        n=3,
    )

    assert result == [
        "payment failed today",
    ]


def test_empty():

    extractor = NGramExtractor()

    assert extractor.extract([], 2) == []


def test_short_sentence():

    extractor = NGramExtractor()

    assert extractor.extract(
        ["payment"],
        2,
    ) == []