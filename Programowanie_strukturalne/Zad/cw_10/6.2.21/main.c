#include <stdio.h>
#include <stdlib.h>

void fun(int ** tab, unsigned n, unsigned m)
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m/2.0; j++)
        {
            int x = tab[i][j];
            tab[i][j]=tab[i][m-j-1];
            tab[i][m-j-1]=x;
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
    tablica[0]=(int*) malloc(sizeof(int)*5);
    tablica[1]=(int*) malloc(sizeof(int)*5);
    wyswietl(tablica, 2, 2);
    fun(tablica, 2, 2);
    wyswietl(tablica, 2, 2);


    return 0;
}
