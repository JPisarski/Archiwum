#include <stdio.h>
#include <stdlib.h>

int ciag(unsigned x)
{
    if (x==0)
    {
        return 1;
    }
    int w = 2*ciag(x-1)+5;
    return w;
}

int main()
{
    unsigned x;
    scanf("%u", &x);
    printf("%d\n", ciag(x));


    return 0;
}
