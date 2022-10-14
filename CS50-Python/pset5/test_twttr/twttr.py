def main():
    # Ask input from user
    sentence = input("Input: ")
    shorten(sentence)
    print("Output: " + shorten(sentence))

# This function expects a str as input and returns that same str without vowels
def shorten(word):
    word_wo_vowels = ""

    # For every letter in input
    for letter in word:

        # If letters in input is a, e, i, o, and u do not print them
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:

            word_wo_vowels += letter

    return word_wo_vowels

if __name__ == "__main__":
    main()





