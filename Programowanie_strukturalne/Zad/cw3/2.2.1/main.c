#include <stdio.h>
#include <stdlib.h>

int bezwgledna(int x)
{
    if(x >= 0)
    {
        return x;
    }
    else
    {
        return -x;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d", bezwgledna(n));

    return 0;
}
