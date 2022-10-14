from um import count

# Does count any um?
def test_um_words():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("instrumentation") == 0
    assert count("umbelliferous") == 0

# Does it case sensitive
def test_case_sensitive():
    assert count("Um,  um, UM...") == 3

# Spaces
def test_spaces():
    assert count("  um  hi") == 1
    assert count("  um?  ") == 1