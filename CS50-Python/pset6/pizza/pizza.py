# Mina Nilay TEZER

import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    try:
        table = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)

        print(tabulate(table, headers="keys", tablefmt="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
