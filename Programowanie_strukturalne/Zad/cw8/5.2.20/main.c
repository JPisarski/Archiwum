#include <stdio.h>
#include <stdlib.h>

char * godzina(int godz, int min, int sek)
{
    char * wynik = malloc(9*sizeof(char));
    sprintf(wynik, "%02d:%02d:%02d", godz, min, sek);
    return wynik;
}

wchar_t * godzina2(int godz, int min, int sek)
{
    wchar_t * wynik = malloc(9*sizeof(wchar_t));
    swprintf(wynik, 9, L"%02d:%02d:%02d", godz, min, sek);
    return wynik;
}

int main()
{
    char * czas = godzina(21,37,00);
    printf("%s\n", czas);
    wchar_t * czas1 = godzina2(7,25,02);
    wprintf(L"%s", czas1);

    return 0;
}
