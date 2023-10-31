#include <stdio.h>
#include <stdlib.h>

void fa(unsigned n, double tab1[n], double tab2[n], double tab3[2*n])  // a)
{
    for(int i=0; i<n; i++)
    {
        tab3[i]=tab1[i];
    }
    for(int i=n; i<2*n; i++)
    {
        for(int j=0; j<n; j++)
        {
            tab3[i]=tab2[j];
        }
    }
}

void fb(unsigned n, double tab1[n], double tab2[n], double tab3[2*n])  // b)
{
    for(int i=1; i<2*n; i+=2)
    {
        for(int j=0; j<n; j++)
        {
            tab3[i]=tab1[j];
        }
    }

    for(int i=0; i<2*n; i+=2)
    {
        for(int j=0; j<n; j++)
        {
            tab3[i]=tab2[j];
        }
    }
}

void wyswietl(int n, double tab[n])
{
    for(int i=0; i<n; i++)
    {
        printf("%lf\n", tab[i]);
    }
}

int main()
{
    double a[5]= {5.0,5.0,5.0,5.0,5.0};
    double b[5]= {0.0,0.0,0.0,0.0,0.0};
    double c[10]= {6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0};
    fa(5, a, b, c);
    wyswietl(10, c);
    fb(5,a,b,c);
    wyswietl(10, c);

    return 0;
}
