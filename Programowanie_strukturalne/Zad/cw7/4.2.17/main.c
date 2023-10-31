#include <stdio.h>
#include <stdlib.h>

double *fun(unsigned n, double tab[n])
{
    double *x = malloc(n*sizeof(double));
    for(int i=0; i<n; i++)
    {
        *(x+i)=tab[i];
    }
    return x;
}



int main()
{
    double tab[4] = {5.0,6.0,7.0,8.0};
    double * x = fun(4,tab);
    printf("%p\n", x);
    printf("%lf\n", *(x));
    printf("%lf\n", *(x+1));
    printf("%lf\n", *(x+2));
    printf("%lf\n", *(x+3));


    return 0;
}
