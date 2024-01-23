#include <stdio.h>
#include <stdlib.h>

void fun(unsigned n, unsigned m, int tab[n][m])
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            tab[i][j]=0;
        }
    }
}

void wyswietl(unsigned n, unsigned m, int tab[n][m])
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            printf("%d\n", tab[i][j]);
        }
    }
}


int main()
{
    int tablica[2][5];
    fun(2, 5, tablica);
    wyswietl(2, 5, tablica);

    return 0;
}
