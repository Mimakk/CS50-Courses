#include <cs50.h>
#include <stdio.h>

long get_number(void);
int length_of_num(long num);
bool checksum(long num);

int main(void)
{
    // Ask the card number
    long num = get_number();

    // Finds the length of the number
    int length = length_of_num(num);

    // Calculates checksum
    bool checksum(long num);

    // To find first and first two digit
    long divisor = 1;
    for (int i = 0; i < length - 1; i++)
    {
        divisor = divisor * 10;
    }

    int firstDigit = num / divisor;
    int firstTwoDigit = num / (divisor / 10);

    // Prints the brand name
    if (checksum(num))
    {
        if (firstDigit == 4 && (length == 13 || length == 16))
        {
            printf("VISA\n");
        }
        else if ((firstTwoDigit == 34 || firstTwoDigit == 37) && length == 15)
        {
            printf("AMEX\n");
        }
        else if ((50 < firstTwoDigit && firstTwoDigit < 56) && length == 16)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
     else
    {
         printf("INVALID\n");
    }


}

// Gets card number from the user
long get_number(void)
{

    long Card_num;
    do
    {
        Card_num = get_long("Number: ");
    }
    while (Card_num <= 0);

    return Card_num;
}

// Finds the length of number
int length_of_num(long num)
{
    int digits = 1;
    while (num >= 10)
    {
        num /= 10; // This is an integer division
        // 1234/10 = 123 => 123/10 = 12 => 12/10 = 1
        digits++ ;
    }
    return digits;

    /* OR can be written as
    int digits = 0;
    while (num != 0)
    {
        num /= 10;
        digits += 1;
    }
    return digits;
    */

}

// Calculates checksum
bool checksum(long num)
{
    long workingCC = num;
    int sum = 0; // this is total sum

// loop for odd numbers
    while (workingCC > 0)
    {
        // lets say our number is 12345
        int lastDigit = workingCC % 10; // this is a modular operator takes last digit 5
        sum += lastDigit; // this adds last digit to sum
        workingCC = workingCC / 100; // intiger dividing byb 100 is gets rid of the last two digit
        // so our number became 123
    }

// loop for even numbers
    workingCC = num / 10; // integer division by 10 gets rid of the last digit
    // we do this because we want even numbers now
    while (workingCC > 0)
    {
        // lets say our number is 12345
        int lastDigit = workingCC % 10; // this is a modular operator takes last digit 5
        int timesTwo = lastDigit * 2;
        sum += (timesTwo % 10) + (timesTwo / 10); // let the number 12 --> (12 % 10 = 2) + (12 / 10 = 1) = 3
        // or you can write a loop and substract 9 untill number < 10
        workingCC = workingCC / 100; // intiger dividing byb 100 is gets rid of the last two digit
        // so our number became 123
    }

    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}







