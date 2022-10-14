# Mina Nilay TEZER

import sys

def main():
    print(line_num())

def line_num():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    number_of_lines = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if (line.lstrip().startswith("#") or line.isspace()==True):
                    pass
                else:
                    number_of_lines += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return number_of_lines

if __name__ == "__main__":
    main()

