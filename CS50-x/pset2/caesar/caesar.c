// Mina Nilay TEZER

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Checking that the program was run with just one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure every character in argv[1] is a digit
    int i = 0;
    while (argv[1][i] != '\0') // till the end itarate over text
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        i++;
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext:  ");

    printf("ciphertext: ");

    // For each character in the plaintext:
    int a = 0;
    while (plaintext[a] != '\0') // till the end itarate over text
    {
        // Rotate the character if it's a letter
        if (isalpha(plaintext[a]))
        {
            printf("%c", rotate(plaintext[a], key));
        }
        else
        {
            printf("%c", plaintext[a]);
        }


        a++;
    }
    printf("\n");
}

char rotate(char c, int n)
{
    // Checks if it's uppercase
    if (isupper(c))
    {
        // Applies formula to ASCII uppercase letters
        c = ((c - 'A' + n) % 26) + 'A';
    }
    // Same, but lowercase
    else
    {
        c = ((c - 'a' + n) % 26) + 'a';
    }
    return c;
}




