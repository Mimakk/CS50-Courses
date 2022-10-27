#include <stdio.h> // includes standart input/output library
#include <cs50.h> // includes cs50's library

int main(void)
{
    // gets name from user
    string name = get_string("What is your name?\n");
    // prints name via place holder 
    printf("Hello, %s!\n", name);
}