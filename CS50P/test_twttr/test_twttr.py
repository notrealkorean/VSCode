from twttr import shorten


def test_word():
    assert shorten("Twitter") == "Twttr"
    assert shorten("0123") == "0123"
    assert shorten("AEI,,OU") == ",,"