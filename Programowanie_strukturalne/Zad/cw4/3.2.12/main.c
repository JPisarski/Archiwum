#include <stdio.h>
#include <stdlib.h>

double * funkcja(unsigned n)
{
    double *x = (double*) calloc(n,sizeof(double));
    return x;
}

int main()
{
    unsigned a;
    scanf("%u", &a);
    double *x = funkcja(a);
    printf("%d\n%lf", x, *x);
    free(x);
    return 0;
}
