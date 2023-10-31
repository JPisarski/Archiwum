#include <stdio.h>
#include <stdlib.h>

int sito(unsigned n)
{
    int tab[n+1];
    for(int i=0; i<n+1; i++)
    {
        tab[i]=0;
    }

    for(int i=2; i*i<=n; i++)
    {
        if(tab[i]==0)
        {
            for(int j=i*i; j<=n; j+=i)
            {
                tab[j]=1;
            }
        }
    }
    int wynik;
    for(int i=0; i<n; i++)
    {
        if(tab[i]==0)
        {
            wynik = i;
        }
    }
    return wynik;
}

int main()
{
    printf("%d\n", sito(10));
    printf("%d\n", sito(100));
    printf("%d", sito(70));
    return 0;
}
