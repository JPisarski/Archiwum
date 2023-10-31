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

void wytnijzw(char nap1[], char nap2[])
{

    int kopia[dlugosc(nap1)];
    for(int t=0; t<dlugosc(nap1); t++)
    {
        kopia[t]=nap1[t];
    }
    for(int j=0; j<dlugosc(nap2); j++)
    {
        for(int k=0; k<dlugosc(nap1); k++)
        {
            if(nap2[j]==nap1[k])
            {
                kopia[k]=-5;
            }
        }
    }
    int m=0;
    for(int w=0; w<dlugosc(nap1); w++)
    {
        if(kopia[w]!=-5)
        {
            nap1[m]=kopia[w];
            m++;
        }
    }
    nap1[m]=0;
}

int main()
{
    char a[] = "Maj";
    char b[] = "Mama";
    wytnijzw(a,b);
    printf("%s\n", a);

    return 0;
}
