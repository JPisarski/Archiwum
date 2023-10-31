#include <stdio.h>
#include <stdlib.h>


int dlugosc(char *x)
{
    int wynik = 0;
    int licznik = 0;
    while(x[licznik]!=0)
    {
        wynik++;
        licznik++;
    }
    return wynik;
}

int porownaj(char *x, char *y)
{
    if(dlugosc(x)==dlugosc(y))
    {
        for(int i=0; i<=dlugosc(x); i++)
        {
            if(x[i]!=y[i])
            {
                return 0;
            }
        }
        return 1;
    }
    else
    {
        return 0;
    }
}


int main()
{
    char *x = "Maj";
    char *y = "Maj";
    printf("%d\n", porownaj(x,y));

    return 0;
}
