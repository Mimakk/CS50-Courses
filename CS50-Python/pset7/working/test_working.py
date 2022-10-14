from working import convert
import pytest


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_time_error():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("14:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 17 PM")

def test_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:40 AM to 5:60 PM")

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM  5 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
