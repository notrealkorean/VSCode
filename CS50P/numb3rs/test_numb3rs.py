from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("275.275.275.275") == False
    assert validate("1.2.3.275") == False
    assert validate("cat") == False