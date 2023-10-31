#include <stdio.h>
#include <stdlib.h>

void zero(unsigned n, int tab[n])  // a)
{
    for(int i=0; i<n; i++)
    {
        tab[i]=0;
    }
}

void indeks(unsigned n, int tab[n])  // b)
{
    for(int i=0; i<n; i++)
    {
        tab[i]=i;
    }
}

void podwojne(unsigned n, int tab[n])  // c)
{
    for(int i=0; i<n; i++)
    {
        tab[i]=2*tab[i];
    }
}

void bezwzgledne(unsigned n, int tab[n])  // d)
{
    for(int i=0; i<n; i++)
    {
        if(tab[i]<0)
        tab[i]=-tab[i];
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
    int tab[5] = {5,5,5,5,5};
    zero(5, tab);
    wyswietl(5,tab);
    indeks(5, tab);
    wyswietl(5,tab);
    podwojne(5, tab);
    wyswietl(5,tab);
    tab[0]= -100;
    bezwzgledne(5, tab);
    wyswietl(5,tab);

    return 0;
}
