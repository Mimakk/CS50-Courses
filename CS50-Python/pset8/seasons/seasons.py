# Mina Nilay TEZER

from datetime import date
import inflect
import sys
import re

p = inflect.engine()


def main():

    birth = input("Date of Birth: ")
    try:
        year, month, day = format_checker(birth)
    except:
        sys.exit("Invalid date")
    today = date.today()
    minutes = minute_calculator(year, month, day, today)

    output = p.number_to_words(minutes, andword="")
    print(output.capitalize() + " minutes")

def format_checker(birth):

    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth):
        year, month, day = birth.split("-")
        return int(year), int(month), int(day)


def minute_calculator(year, month, day, today):

    birth_date = date(year, month, day)
    time_passed = today - birth_date
    minutes = time_passed.days * 24 * 60
    return str(minutes)

if __name__ == "__main__":
    main()