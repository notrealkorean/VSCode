from seasons import calc
from pytest import raises


def test_test():
    assert calc("1999-01-01") == "Twelve million, eight hundred fifty-two thousand minutes"