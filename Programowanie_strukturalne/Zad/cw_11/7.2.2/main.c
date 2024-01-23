#include <stdio.h>
#include <stdlib.h>


struct trojkat
{
    int bok_1;
    int bok_2;
    int bok_3;
};

void przepisz(struct trojkat troj1, struct trojkat *troj2)
{
    troj2 ->bok_1 = troj1.bok_1;
    troj2 ->bok_2 = troj1.bok_2;
    troj2 ->bok_3 = troj1.bok_3;
}

int main()
{
    struct trojkat zmiennaS1 = {6,6,6};
    struct trojkat zmiennaS2 = {5,5,5};
    struct trojkat *wsk = &zmiennaS2;
    przepisz(zmiennaS1, wsk);
    printf("%d\n%d\n%d\n", zmiennaS2.bok_1, zmiennaS2.bok_2, zmiennaS2.bok_3);
    return 0;
}
