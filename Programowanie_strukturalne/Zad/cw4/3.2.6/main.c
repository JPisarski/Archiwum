#include <stdio.h>
#include <stdlib.h>

void funkcja(int n, int *w)
{
    *w = n;
}

int main()
{
    int x,y;
    scanf("%d", &x);
    scanf("%d", &y);
    funkcja(x, &y);
    printf("%d, %d\n", x, y);
    return 0;
}
