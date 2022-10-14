from plates import is_valid

def test_two_letter():
    assert is_valid("HI") == True
    assert is_valid("H1") == False
    assert is_valid("1H") == False
    assert is_valid("11") == False
    assert is_valid("5HI") == False
    assert is_valid("50HI") == False

def test_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False

def test_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_firstnum():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punc():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3?14") == False
    assert is_valid("PI3 14") == False