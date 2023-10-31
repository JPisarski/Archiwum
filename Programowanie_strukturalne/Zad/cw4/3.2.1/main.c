#include <stdio.h>
#include <stdlib.h>

int funkcja(int *x, int *y)
{
    if(*x<*y)
    {
        return *x;
    }
    else if(*y<*x)
    {
        return *y;
    }
    else
    {
        printf("Obie liczby s¹ równe i wynosz¹: \n");
        return *x;
    }
}

int main()
{
    int x,y;
    scanf("%d", &x);
    scanf("%d", &y);
    printf("%d\n", funkcja(&x,&y));
    return 0;
}
