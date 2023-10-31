#include <stdio.h>
#include <stdlib.h>

void fun(int **tab, unsigned n, unsigned m)
{
    for(int i=0; i<n; i++)
    {
        int x = tab[i][m-1];
        for(int j=m-1; j>0; j--)
        {
            tab[i][j]=tab[i][j-1];
        }
        tab[i][0]=x;
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
    tablica[0]=(int*) malloc(sizeof(int)*5);
    tablica[1]=(int*) malloc(sizeof(int)*5);
    wyswietl(tablica, 2, 5);
    fun(tablica, 2, 5);
    wyswietl(tablica, 2, 5);


    return 0;
}
