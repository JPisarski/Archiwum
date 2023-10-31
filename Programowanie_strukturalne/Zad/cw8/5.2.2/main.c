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

int dlugosc5(wchar_t *x)
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

int main()
{
    char *x = "1234567";
    printf("%d\n", dlugosc(x));
    wchar_t *y = L"1absffj";
    printf("%d\n", dlugosc5(y));

    return 0;
}



