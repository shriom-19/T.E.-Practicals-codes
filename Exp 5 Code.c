
clc;

g=7;
p=23;

printf("\n The results are as follows:\n\n");

x=3;
y=6;

R1=modulo(g^x,p);
R2=modulo(g^y,p);

printf("1)Alice choose x=%d & calculates R1=%d\n\n2)Bob chooses y=%d & calculates R2=%d\n\n3)Alice sends the number %d to Bob \n\n4)Bob sends the number %d to Alice \n\n",x,R1,y,R2,R1,R2);

K_Alice=modulo((R2)^x,p);
K_Bob=modulo((R1)^y,p);

K_Final=modulo(g^(x*y),p);

printf("5)Alice calculates the symmetric key K=%d \n\n6)Bob calculates the symmetric key k=%d\n\n7)K_Final=%d \n\n",K_Alice,K_Bob,K_Final);
