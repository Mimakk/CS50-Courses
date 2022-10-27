#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int c;
    do
    {
        c = get_int("Enter the cents: ");
    }
    while (c < 0);
    return c;
}

int calculate_quarters(int cents)
{
    int i = 0;
    // checks is cents bigger than 25
    if (cents >= 25)
    {
        // in every loop substract 25
        while (cents >= 25)
        {
            cents -= 25;
            i++;
        }
    }
    return i;
}

int calculate_dimes(int cents)
{
    int i = 0;
    // checks is cents bigger than 10
    if (cents >= 10)
    {
        // in every loop substract 10
        while (cents >= 10)
        {
            cents -= 10;
            i++;
        }
    }
    return i;
}

int calculate_nickels(int cents)
{
    int i = 0;
    // checks is cents bigger than 5
    if (cents >= 5)
    {
        // in every loop substract 5
        while (cents >= 5)
        {
            cents -= 5;
            i++;
        }
    }
    return i;
}

int calculate_pennies(int cents)
{
    int i = 0;
    // checks is cents bigger than 1
    if (cents >= 1)
    {
        // in every loop substract 1
        while (cents >= 1)
        {
            cents -= 1;
            i++;
        }
    }
    return i;
}
