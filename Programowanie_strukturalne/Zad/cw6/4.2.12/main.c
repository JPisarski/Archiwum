#include <stdio.h>
#include <stdlib.h>

void fun(unsigned n, int tab[n]) // a)
{
    int a[n];
    for(int i=0; i<n; i++)
    {
        a[i]=tab[i];
    }

    for(int i=0; i<n; i++)
    {
        tab[i]=a[n-1-i];
    }
}

void wlewo(unsigned n, int tab[n]) // b)
{
    int a[n];
    for(int i=0; i<n; i++)
    {
        a[i]=tab[i];
    }

    for(int i=0; i<n; i++)
    {
        tab[i]=a[i+1];
    }
    tab[n-1]=a[0];
}

void wprawo(unsigned n, int tab[n]) // c)
{
    int a[n];
    for(int i=0; i<n; i++)
    {
        a[i]=tab[i];
    }

    for(int i=0; i<n; i++)
    {
        tab[i]=a[i-1];
    }
    tab[0]=a[n-1];
}

void ros(unsigned n, int tab[n]) // d)
{
    for(int i=0; i<n; i++)
    {
        for(int j=1; j<n-i; j++)
        {
            if(tab[j-1]>tab[j])
            {
                int a = tab[j-1];
                tab[j-1]=tab[j];
                tab[j]=a;
            }
        }
    }
}

void mal(unsigned n, int tab[n]) // e)
{
    for(int i=0; i<n; i++)
    {
        for(int j=1; j<n-i; j++)
        {
            if(tab[j-1]<tab[j])
            {
                int a = tab[j-1];
                tab[j-1]=tab[j];
                tab[j]=a;
            }
        }
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
    int a[5]= {1,2,3,4,5};
    fun(5, a);
    wyswietl(5, a);
    wlewo(5,a);
    wyswietl(5, a);
    wprawo(5, a);
    wyswietl(5, a);
    ros(5, a);
    wyswietl(5, a);
    mal(5, a);
    wyswietl(5, a);
    return 0;
}
