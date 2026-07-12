from app.preprocessing.text_cleaner import TextCleaner


def test_lowercase():
    cleaner = TextCleaner()
    assert cleaner.clean("PAYMENT FAILED") == "payment failed"


def test_trim_spaces():
    cleaner = TextCleaner()
    assert cleaner.clean("   payment failed   ") == "payment failed"


def test_multiple_spaces():
    cleaner = TextCleaner()
    assert cleaner.clean("payment     failed") == "payment failed"


def test_new_lines():
    cleaner = TextCleaner()
    assert cleaner.clean("payment\nfailed") == "payment failed"


def test_keep_emoji():
    cleaner = TextCleaner()
    assert cleaner.clean("PAYMENT 😡") == "payment 😡"