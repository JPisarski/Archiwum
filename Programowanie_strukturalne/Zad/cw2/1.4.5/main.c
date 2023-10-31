#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);

    int suma = 0;

    for(int i=0; i<=n; i++)
    {
        suma += pow(i,2);
    }

    printf("%d", suma);



    return 0;
}
