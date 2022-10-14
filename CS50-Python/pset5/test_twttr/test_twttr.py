from twttr import shorten

def test_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_capital():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("?.,!") == "?.,!"