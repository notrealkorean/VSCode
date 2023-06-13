from fuel import convert, gauge
from pytest import raises

def test_fraction():
    with raises(ValueError):
        convert("10/1")

    with raises(ZeroDivisionError):
        convert("10/0")

    with raises(ValueError):
        convert("cat/dog")

    assert convert("1/2") == 50

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(99) == "F"
