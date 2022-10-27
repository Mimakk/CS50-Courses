#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Enter a number between 1 and 8: \n");
    }
    while (n < 1 || n > 8);
    for (int i = 1 ; i < n + 1 ; i++) //started from 1 because when i start from 0
    //because 0 is not < 0 code gives an empty line
    {
        //this loop starts from n untill i and subrtacts 1 in every iteration
        for (int k = n ; k > i ; k--)
        {
            printf(" "); //prints (" ") n-i times
        }
        //this loop starts from 0 to i and add 1 in every iteration
        for (int j = 0 ; j < i ; j++)
        {
            printf("#");
        }
        printf("\n"); //to get a new line
    }
}