#include <stdio.h>
#include <stdlib.h>


void zamiana(int *x, int *y)
{
    int z = *x;
    *x = *y;
    *y = z;
}

int main()
{
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);

    zamiana(&a, &b);
    printf("%d\n%d\n", a, b);

    // przypadek testowy

    int x = 10;
    int y = 5;
    zamiana(&x, &y);
    printf("%d\n%d\n", x, y);


    return 0;
}
