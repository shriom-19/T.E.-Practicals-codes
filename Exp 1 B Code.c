// “Design and implement for the insecurity of default passwords, printed passwords and password transmitted in plain text.”
//Printed Passwords


#include <stdio.h>

int main()
{
    char password[10], username[10];
    int i;

    printf("Enter User name: ");
    scanf("%s", username);

    printf("Enter the password (any 8 characters): ");

    for(i = 0; i < 8; i++)
    {
        password[i] = getchar();   // take input
        if(password[i] == '\n')    // skip newline
        {
            i--;
            continue;
        }
        printf("*");               // print star
    }

    password[i] = '\0';

    printf("\nYour password is: %s\n", password);

    return 0;
}