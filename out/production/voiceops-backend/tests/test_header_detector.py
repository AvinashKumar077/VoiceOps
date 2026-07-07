from app.parsers.header_detector import HeaderDetector


def test_detect_google_play_headers():

    detector = HeaderDetector()

    mapping = detector.detect([
        "reviewId",
        "userName",
        "content",
        "score",
        "at"
    ])

    assert mapping.id_column == "reviewId"
    assert mapping.text_column == "content"
    assert mapping.rating_column == "score"
    assert mapping.date_column == "at"