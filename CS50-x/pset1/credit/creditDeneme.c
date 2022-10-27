#include <cs50.h>
#include <stdio.h>

long get_number(void);
long length_of_num();

int main(void)
{
    // Ask the card number
    long Card_num;
    do
    {
        Card_num = get_long("Number: ");
    }
    while (Card_num <= 0);

    return Card_num;
    printf("num in main: %li\n", num);

    // Finds the length of the number
    long length = length_of_num();
    printf("Lenght: %li\n", length);


}

// gets card number from the user
long get_number(void)
{


}

long length_of_num(long num)
{
    int digits = 1;
    printf("num before loop: %li\n", num);
    while (num >= 10)
    {
        printf("num before division: %li\n", num);
        num /= 10; // This is an integer division
        printf("num after division: %li\n", num);
        // 1234/10 = 123 => 123/10 = 12 => 12/10 = 1
        digits++ ;
        printf("Digits in every loop: %i\n", digits);

    }
    return digits;
}
