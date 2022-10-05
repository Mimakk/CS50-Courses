# Mina Nilay TEZER

camelCase = input("camelCase: ")

for letter in camelCase:
    if (letter.isupper()) == True:
        lower_letter = letter.lower()
        print("_", lower_letter, sep='', end="")
    else:
        print(letter, end="")

print()