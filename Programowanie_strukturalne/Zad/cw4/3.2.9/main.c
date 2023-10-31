#include <stdio.h>
#include <stdlib.h>

int * funkcja(void)
{
    int *x = (int*) malloc(sizeof(int));
    return x;

}

int main()
{
    int *x = funkcja();
    printf("%d\n%d", x, *x);
    free(x);
    return 0;
}
