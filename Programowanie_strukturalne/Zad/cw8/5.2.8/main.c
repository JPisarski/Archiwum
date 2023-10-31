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

void podmien(char a[])
{
    for(int i=0; i<dlugosc(a); i++)
    {
        if(a[i]<= 122 && a[i]>= 97)
        {
            a[i]-= 32;
        }
    }
}



int main()
{
    char x[] = "Jakub Pisarski";
    podmien(x);
    printf("%s\n", x);

    return 0;
}
