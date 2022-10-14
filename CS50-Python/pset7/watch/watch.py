# Mina Nilay TEZER

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe(.)*><\/iframe>$", s, re.IGNORECASE):
        if url := re.search(r"(https?:\/\/(www\.)?youtube\.com\/embed\/)([a-zA-Z0-9]+)", s):
            groups = url.groups()
            return "https://youtu.be/" + groups[2]


if __name__ == "__main__":
    main()