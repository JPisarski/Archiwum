#include <stdio.h>
#include <stdlib.h>

void fun(int ** tab, unsigned n, unsigned m)
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            tab[i][j]=0;
        }
    }
}

void wyswietl(int **tab, unsigned n, unsigned m)
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
    int **tablica= (int**) malloc(sizeof(int*)*2);
    tablica[0]=(int*) malloc(sizeof(int)*2);
    tablica[1]=(int*) malloc(sizeof(int)*2);
    fun(tablica,2,5);
    wyswietl(tablica, 2, 5);

    return 0;
}
