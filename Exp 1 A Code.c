// “Design and implement for the insecurity of default passwords, printed passwords and password transmitted in plain text.”
//Default Passwords


// output-
// Enter your username:
// admin
// Enter your password:
// admin
//  Welcome.Login Success!


// code-
#include <stdio.h>
#include <string.h>


int main()
{
    char username[15];
    char password[12];

    printf("Enter your username:\n");
    scanf("%s",&username);

    printf("Enter your password:\n");
    scanf("%s",&password);

    if(strcmp(username,"admin")==0)
    {
        if(strcmp(password,"admin")==0)
        {
            printf("\n Welcome.Login Success!");
        }
        else
        {
            printf("\nwrong password");
        }
    }
    else
    {
        printf("\n User doesn't exist");
    }

    return 0;
}