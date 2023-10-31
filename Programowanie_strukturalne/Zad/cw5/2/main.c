#include <stdio.h>
#include <stdlib.h>

int funkcja(unsigned n)
{
    if(n==0 || n==1)
    {
        return 2;
    }
    else if(n%2==0)
    {
        return funkcja((n/2)-1)+(n/2);
    }
    else
    {
        return 2*funkcja(n-1)-((n-1)/2);
    }
}


int main()
{
    unsigned n;
    scanf("%u", &n);
    printf("%d\n", funkcja(n));

    //przypadek testowy

    printf("%d\n", funkcja(6));
    printf("%d\n", funkcja(7));


    return 0;
}
