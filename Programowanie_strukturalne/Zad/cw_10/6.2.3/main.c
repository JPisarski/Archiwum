#include <stdio.h>
#include <stdlib.h>

void fun(unsigned n, unsigned m, int **tab)
{
    for(int i=0; i<n; i++)
    {
        free(tab[i]);
    }
    free(tab);
}

int main()
{
    int **tablica= (int**) malloc(sizeof(int*)*2);
    tablica[0]=(int*) malloc(sizeof(int)*5);
    tablica[1]=(int*) malloc(sizeof(int)*5);
    fun(2, 5, tablica);

    return 0;
}
