#include <stdio.h>
#include <stdlib.h>

int fun(unsigned n, int tab[n][100][100])
{
    int wynik = 0;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<100; j++)
        {
            for(int k=0; k<100; k++)
            {
                wynik +=tab[i][j][k];
            }
        }
    }
    return wynik;
}

int main()
{
    int tablica[2][100][100];
    printf("%d\n", fun(2,tablica));

    return 0;
}
