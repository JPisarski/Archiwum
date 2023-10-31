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

void kopiujn(char nap1[], char nap2[], unsigned n)
{
    if(n<=dlugosc(nap1))
    {
        for(int i=0; i<n; i++)
        {
            nap2[i]=nap1[i];
        }
    }
    else
    {
        for(int i=0; i<dlugosc(nap1); i++)
        {
            nap2[i]=nap1[i];
        }
    }
    nap2[dlugosc(nap2)]=0;
}

int main()
{
    char x[] = "Maj";
    char y[]= "Lipiec";
    kopiujn(x,y,5);
    y[dlugosc(y)]=0;
    printf("%s\n", y);
    return 0;
}
