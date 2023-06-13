from plates import is_valid

def test_correct():
    assert is_valid("CS50") == True
    assert is_valid("CSCSCS") == True
    assert is_valid("CSCS50") == True

def test_start():
    assert is_valid("5340") == False
    assert is_valid("CS50P") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("CASDADSD") == False
def test_sequence():
    assert is_valid("AAA22A") == False
    assert is_valid("AA022") == False

def test_punct():
    assert is_valid("CSC '.50") == False
    assert is_valid(".,.'") == False
    assert is_valid("PI3.14") == False
    assert is_valid("0UTATIME") == False
    assert is_valid("0ASA") == False
    assert is_valid("H") == False