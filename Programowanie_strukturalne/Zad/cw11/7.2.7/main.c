#include <stdio.h>
#include <stdlib.h>


struct zespolone
{
    double re;
    double im;
};

struct zespolone dodaj(struct zespolone a, struct zespolone b)
{
    struct zespolone wynik = {a.re+b.re,a.im+b.im};
    return wynik;
};

int main()
{
    struct zespolone liczba1 = {9.5,9.5};
    struct zespolone liczba2 = {5.5,5.5};
    struct zespolone suma = dodaj(liczba1, liczba2);
    printf("%lf+%lfi\n", suma.re, suma.im);

    return 0;
}
