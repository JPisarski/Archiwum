#include <stdio.h>
#include <stdlib.h>


void fun(int **tab, unsigned n, unsigned m)
{
    for(int  i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            printf("%d  ", tab[j][i]);
        }
        printf("\n");
    }
}

int main()
{
    int **tablica= (int**) malloc(sizeof(int*)*2);
    tablica[0]=(int*) malloc(sizeof(int)*2);
    tablica[1]=(int*) malloc(sizeof(int)*2);
    fun(tablica, 2, 2);

    return 0;
}
