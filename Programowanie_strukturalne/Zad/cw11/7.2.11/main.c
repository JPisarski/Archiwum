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
    printf("Je�li chcesz poda� liczb� ca�kowit�, wpisz 0\nJe�li chcesz poda� liczb� wymiern�, wpisz 1: ");
    scanf("%d", &wynik.tp);
    if (wynik.tp==0)
    {
        printf("Podaj liczb� ca�kowit�: ");
        scanf("%d", &wynik.zaw.a);
    }
    else
    {
        printf("Podaj liczb� wymiern�: ");
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
