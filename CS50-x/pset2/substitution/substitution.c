// Mina Nilay TEZER

// Importing libraries
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// Declaring functions
bool validate_key(string key);
void encipher(string key, string plaintext);

int main(int argc, string argv[])
{
    // Checking that the program was run with just one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Declaring argv[1] as key
    string key = argv[1];

    // If validate_key true get plaintext from user
    if (validate_key(key) == 0)
    {
        // Prompt user for plaintext
        string plaintext = get_string("plaintext:  ");

        // Convert all alphabets in the key to uppercase
        for (int i = 0; i < strlen(key); i++)
        {
            if (islower(key[i]))
            {
                key[i] = key[i] - 32;
            }
        }

        encipher(key, plaintext);
    }
    else
    {
        return 1;
    }


}

// This function validates the key taken from user
bool validate_key(string key)
{
    // Checking is the key has the length of 26
    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // This while loop checks every char of key
    int i = 0;
    while (key[i] != '\0') // till the end itarate over text
    {
        // Make sure every character in argv[1] is contains only alphabetical characters
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetical characters.\n");
            return 1;
        }
        // Looks for the repeated char
        for (int j = i + 1 ; j < strlen(key) ; j++) // checking to the next element of arg[i]
        {
            if (toupper(key[j]) == toupper(key[i])) // checking repeated element
            {
                printf("Key must not contain repeated alphabets.\n");
                return 1;
            }
        }
        i++;
    }
    return 0;
}

void encipher(string key, string plaintext)
{
    //string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Alphabet array

    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            int letter = plaintext[i] - 65;
            printf("%c", key[letter]);
        }
        else if (islower(plaintext[i]))
        {
            int letter = plaintext[i] - 97;
            printf("%c", key[letter] + 32);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}



