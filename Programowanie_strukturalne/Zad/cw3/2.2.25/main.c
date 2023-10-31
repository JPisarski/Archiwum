#include <stdio.h>
#include <stdlib.h>

int ciag(unsigned x)
{
    int w = 1;
    if(x == 1 || x == 0)
    {
        return 1;
    }

    if(x%2==0)
    {
        w = ciag(x-1)+x;
        return w;
    }
    else
    {
        w = ciag(x-1)*x;
        return w;
    }
}

int main()
{
    unsigned n;
    scanf("%u", &n);
    printf("%d", ciag(n));


    return 0;
}
