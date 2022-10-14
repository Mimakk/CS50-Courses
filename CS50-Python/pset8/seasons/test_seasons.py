from seasons import minute_calculator, format_checker
import datetime

def test_format():
    assert format_checker("1998-05-28") == (1998, 0o05, 28)
    assert format_checker("1998-5-28") == None
    assert format_checker("May 28, 1998") == None


# minute_calculator(year, month, day, today)
# datetime.date(2019, 4, 13)
def test_minute():
    assert minute_calculator(1998, 0o06, 20, datetime.date(2000, 0o01, 0o01)) == "806400"
    assert minute_calculator(2020, 0o06, 0o01, datetime.date(2032, 0o01, 0o01)) == "6092640"
