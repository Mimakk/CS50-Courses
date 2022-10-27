// Mina Nilay TEZER

// importing libraries
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

// declaring functions
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
float equation(float letters_per_100, float sentences_per_100);


int main(void)
{
    // take the text from user
    string text = get_string("Text: ");

    // declare letters, words and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    //printf("letters %i words %i sentences %i\n", letters, words, sentences);

    // calculate letters and sentences per 100 words
    float letters_per_100 = 100 * ((float)letters / (float)words);
    float sentences_per_100 = 100 * ((float)sentences / (float)words);

    // calculating index
    float index = equation(letters_per_100, sentences_per_100);

    // printing grade according to index
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (1 <= round(index) && round(index) < 16)
    {
        printf("Grade %i\n", (int)round(index));
    }
    else if (16 <= index)
    {
        printf("Grade 16+\n");
    }
}

// this function calculates hoe many letters in text
int count_letters(string text)
{
    int letters = 0;
    int i = 0;
    while (text[i] != '\0') // till the end itarate over text
    {
        if (isalpha(text[i])) // is alphabetical character
        {
            letters++;
        }
        i++;
    }
    return letters;
}

// this function calculates how many words in text
int count_words(string text)
{
    int words = 1;
    int i = 0;
    while (text[i] != '\0') // till the end itarate over text
    {
        if (isspace(text[i])) // is space
        {
            words++;
        }
        i++;
    }
    return words;

}

// this function calculates how many sntences in text
int count_sentences(string text)
{
    int sentences = 0;
    int i = 0;
    while (text[i] != '\0') // till the end itarate over text
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
        i++;
    }
    return sentences;

}

// this function calculates the index
float equation(float letters_per_100, float sentences_per_100)
{
    float index = 0.0588 * letters_per_100 - 0.296 * sentences_per_100 - 15.8;
    
    return index;
}

