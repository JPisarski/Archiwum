#include <stdio.h>
#include <stdlib.h>

void fun(double *x)
{
    free(x);
}

int main()
{
    double * tab = malloc(5*sizeof(double));
    fun(tab);
    return 0;
}
