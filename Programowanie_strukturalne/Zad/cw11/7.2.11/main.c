#include <stdio.h>
#include <stdlib.h>

union Liczba
{
    int a;
    float b;
};

struct Dane
{
    int tp;
    union Liczba zaw;
};

struct Dane funkcja()
{
    struct Dane wynik;
    printf("Jeœli chcesz podaæ liczbê ca³kowit¹, wpisz 0\nJeœli chcesz podaæ liczbê wymiern¹, wpisz 1: ");
    scanf("%d", &wynik.tp);
    if (wynik.tp==0)
    {
        printf("Podaj liczbê ca³kowit¹: ");
        scanf("%d", &wynik.zaw.a);
    }
    else
    {
        printf("Podaj liczbê wymiern¹: ");
        scanf("%f", &wynik.zaw.b);
    }
    return wynik;
}

int main()
{
    struct Dane abc = funkcja();
    if(abc.tp==0)
    {
        printf("%d\n%d\n", abc.tp, abc.zaw.a);
    }
    else
    {
        printf("%d\n%f\n", abc.tp, abc.zaw.b);
    }


    return 0;
}
