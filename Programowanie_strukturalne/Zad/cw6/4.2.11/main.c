#include <stdio.h>
#include <stdlib.h>

double iloczyn(unsigned n, double tab1[n], double tab2[n])
{
    double wynik = 0;
    for(int i=0; i<n; i++)
    {
        wynik += tab1[i]*tab2[i];
    }
    return wynik;
}


int main()
{
    double a[5] = {1.0,1.0,1.0,1.0,1.0};
    double b[5] = {5.0,5.0,5.0,5.0,5.0};
    printf("%lf\n", iloczyn(5, a, b));
    return 0;
}
