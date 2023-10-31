#include <stdio.h>
#include <stdlib.h>

int * funkcja(unsigned n)
{
    int *x = (int*) calloc(n,sizeof(int));
    return x;
}

int main()
{
    unsigned a;
    scanf("%u", &a);
    int *x = funkcja(a);
    printf("%d\n%d", x, *x);
    free(x);
    return 0;
}
