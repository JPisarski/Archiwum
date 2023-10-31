#include <stdio.h>
#include <stdlib.h>

void fun(unsigned n, unsigned m, int tab[n][m])
{
    free(tab);
}

int main()
{
    // b³¹d???
    int tablica[2][2]={{5,5},{6,6}};
    fun(2, 2, tablica);
    return 0;
}
