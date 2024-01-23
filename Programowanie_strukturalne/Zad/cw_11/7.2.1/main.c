#include <stdio.h>
#include <stdlib.h>


struct trojkat
{
    int bok_1;
    int bok_2;
    int bok_3;
};

int obwod(struct trojkat zmienna)
{
    return zmienna.bok_1+zmienna.bok_2+zmienna.bok_3;
}

int main()
{
    struct trojkat zmiennaS;
    zmiennaS.bok_1=6;
    zmiennaS.bok_2=6;
    zmiennaS.bok_3=6;
    printf("%d\n", obwod(zmiennaS));

    return 0;
}
