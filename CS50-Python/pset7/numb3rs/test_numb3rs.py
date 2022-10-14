from numb3rs import  validate

def test_range():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1000.1.1.1") == False
    assert validate(r"1.1000.1.1") == False
    assert validate(r"1.1.1000.1") == False
    assert validate(r"1.1.1.1000") == False
    assert validate(r"10.1.355.0") == False


def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"1.2.3.4.5") == False
