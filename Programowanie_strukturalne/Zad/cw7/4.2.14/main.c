#include <stdio.h>
#include <stdlib.h>


double *fun(unsigned n)
{
    double * tab = malloc(n*sizeof(double));
    return tab;
}

int main()
{
    double *x = fun(5);
    printf("%p\n", x);
    return 0;
}
