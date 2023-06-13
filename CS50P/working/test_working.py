from working import convert
from pytest import raises


def test_convert():
    with raises(ValueError):
        convert("9:70 AM to 5:70 PM")
    with raises(ValueError):
        convert("9 AM - 5 PM")

    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"