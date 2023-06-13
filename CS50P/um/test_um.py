from um import count

def test_count():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("  um  ") == 1
    assert count("a um a") == 1
    assert count("yummy") == 0