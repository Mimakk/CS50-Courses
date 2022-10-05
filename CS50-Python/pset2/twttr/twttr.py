# Mina Nilay TEZER

# Ask input from user
sentence = input("Input: ")

print("Output: ", end="")
# For every letter in input
for letter in sentence:

    # If letters in input is a, e, i, o, and u do not print them
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:

        print(letter, end="")

print()