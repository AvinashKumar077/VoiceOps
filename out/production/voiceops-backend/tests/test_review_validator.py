from app.preprocessing.review_validator import ReviewValidator


validator = ReviewValidator()


def test_valid_review():
    assert validator.is_valid("Payment failed")


def test_none_review():
    assert not validator.is_valid(None)


def test_empty_review():
    assert not validator.is_valid("")


def test_spaces_review():
    assert not validator.is_valid("      ")


def test_single_character():
    assert not validator.is_valid("a")


def test_two_characters():
    assert validator.is_valid("ok")