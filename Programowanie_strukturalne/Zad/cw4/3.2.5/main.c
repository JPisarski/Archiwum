#include <stdio.h>
#include <stdlib.h>

int funkcja(int const *x, int const *y)
{
    return *x+*y;
}

int main()
{
    int x,y;
    scanf("%d", &x);
    scanf("%d", &y);
    printf("%d\n", funkcja(&x,&y));
    return 0;
}
