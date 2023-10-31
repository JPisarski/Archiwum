#include <stdio.h>
#include <stdlib.h>

void suma(unsigned n, int tab1[n], int tab2[n], int tab3[n]) // a)
{
    for(int i=0; i<n; i++)
    {
        tab3[i] = tab2[i]+tab1[i];
    }
}

void wieksze(unsigned n, int tab1[n], int tab2[n], int tab3[n])  // b)
{
    for(int i=0; i<n; i++)
    {
        if(tab2[i]>tab1[i])
        {
            tab3[i] = tab2[i];
        }
        else
        {
            tab3[i]=tab1[i];
        }
    }
}

void zamiana(unsigned n, int tab1[n], int tab2[n], int tab3[n])   // c)
{
    int a[n];
    int b[n];

    for(int i=0; i<n; i++)
    {
        a[i]=tab1[i];
    }
    for(int i=0; i<n; i++)
    {
        b[i]=tab2[i];
    }

    for(int i=0; i<n; i++)
    {
        tab1[i]=tab3[i];
    }
    for(int i=0; i<n; i++)
    {
        tab2[i]=a[i];
    }
    for(int i=0; i<n; i++)
    {
        tab3[i]=b[i];
    }
}

void wyswietl(int n, int tab[n])
{
    for(int i=0; i<n; i++)
    {
        printf("%d\n", tab[i]);
    }
}

int main()
{
    int a[5]={5,5,5,5,5};
    int b[5]={10,10,10,10,10};
    int c[5]={5,5,5,5,5};

    suma(5, a, b, c);
    wyswietl(5, c);
    wieksze(5, a, b, c);
    wyswietl(5, c);
    zamiana(5, a, b, c);
    wyswietl(5, a);
    wyswietl(5, b);
    wyswietl(5, c);

    return 0;
}
