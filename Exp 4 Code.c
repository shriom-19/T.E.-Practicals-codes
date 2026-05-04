// “RSA Implementation of Symmetric and Asymmetric Cryptography”

// output-
// ENTER FIRST PRIME NUMBER
// 11

// ENTER ANOTHER PRIME NUMBER
// 7

// POSSIBLE VALUES OF e AND d ARE

// 13	37
// 17	53
// 19	19
// 23	47
// 29	29
// 31	31
// 37	13
// 41	41
// 43	7
// 47	23
// 53	17
// 59	59
// ENTER MESSAGE
// Sinhgad

// THE ENCRYPTED MESSAGE IS
// 7����a�
// THE DECRYPTED MESSAGE IS
// Sinhgad

// code-
#include<stdio.h>
#include<string.h>
#include<math.h>

int prime(long int);
void ce();
long int cd(long int);
void encrypt();
void decrypt();

long int p,q,n,t,flag,e[100],d[100],temp[100],j,m[100],en[100],i;
char msg[100];

int main()
{
    printf("\nENTER FIRST PRIME NUMBER\n");
    scanf("%ld",&p);

    printf("\nENTER ANOTHER PRIME NUMBER\n");
    scanf("%ld",&q);

    n=p*q;
    t=(p-1)*(q-1);

    ce();

    printf("\nPOSSIBLE VALUES OF e AND d ARE\n");
    for(i=0;i<j;i++)
    {
        printf("\n%ld\t%ld",e[i],d[i]);
    }

    printf("\nENTER MESSAGE\n");
    scanf("%s",msg);

    for(i=0;msg[i]!='\0';i++)
        m[i]=msg[i];

    encrypt();
    decrypt();

    // optional pause (replacement of getch)
    getchar(); getchar();

    return 0;
}

int prime(long int pr)
{
    int i;
    int j=sqrt(pr);

    for(i=2;i<=j;i++)
    {
        if(pr%i==0)
            return 0;
    }
    return 1;
}

void ce()
{
    int k=0;

    for(i=2;i<t;i++)
    {
        if(t%i==0)
            continue;

        flag=prime(i);

        if(flag==1 && i!=p && i!=q)
        {
            e[k]=i;
            flag=cd(e[k]);

            if(flag>0)
            {
                d[k]=flag;
                k++;
            }

            if(k==99)
                break;
        }
    }
    j=k;
}

long int cd(long int x)
{
    long int k=1;

    while(1)
    {
        k=k+t;
        if(k%x==0)
            return(k/x);
    }
}

void encrypt()
{
    long int pt,ct,key=e[0],k,len;

    i=0;
    len=strlen(msg);

    while(i!=len)
    {
        pt=m[i];
        pt=pt-96;

        k=1;

        for(j=0;j<key;j++)
        {
            k=(k*pt)%n;
        }

        temp[i]=k;
        ct=k+96;
        en[i]=ct;

        i++;
    }

    en[i]=-1;

    printf("\nTHE ENCRYPTED MESSAGE IS\n");
    for(i=0;en[i]!=-1;i++)
        printf("%c",en[i]);
}

void decrypt()
{
    long int pt,ct,key=d[0],k;

    i=0;

    while(en[i]!=-1)
    {
        ct=temp[i];

        k=1;

        for(j=0;j<key;j++)
        {
            k=(k*ct)%n;
        }

        pt=k+96;
        m[i]=pt;

        i++;
    }

    m[i]=-1;

    printf("\nTHE DECRYPTED MESSAGE IS\n");
    for(i=0;m[i]!=-1;i++)
        printf("%c",m[i]);
}