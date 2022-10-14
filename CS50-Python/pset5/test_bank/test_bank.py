from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello Mina") == 0
    assert value("hello mina") == 0

def test_h():
    assert value("Hi") == 20
    assert value("hey") == 20

def test_other():
    assert value("What’s up") == 100
    assert value("good morning") == 100