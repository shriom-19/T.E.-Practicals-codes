// “IMPLEMENTATION OF MONOALPHABETIC CIPHER”



// output-
// Enter plain text:helloworld

// After Encryption:
// ---------------------

// YAMMEUEWMS
// After Decryption:
// ---------------------

// helloworld



// code-
#include<stdio.h>
#include<string.h>

#define pf printf
#define sf scanf

char dcl[26]="XDGSAZNYOBTMJCEVFWKPLQUR";
char ecl[26]="abcdefghijklmnopqrstuvwxyz";

void e(char*);
void d(char*);

int main()
{
    char p[100];   

    pf("\nEnter plain text:");
    sf("%s", p);

    pf("\nAfter Encryption:\n---------------------\n");
    e(p);
    pf("\n%s", p);

    pf("\nAfter Decryption:\n---------------------\n");
    d(p);
    pf("\n%s", p);

    return 0;
}

void e(char *p)
{
    int i=0;
    while(*(p+i)!='\0')
    {
        *(p+i)=dcl[*(p+i)-97];
        i++;
    }
}

void d(char *p)
{
    int i=0,j;
    while(*(p+i)!='\0')
    {
        for(j=0;j<26;j++)
        {
            if(dcl[j]==*(p+i))
                break;
        }
        *(p+i)=ecl[j];
        i++;
    }
}