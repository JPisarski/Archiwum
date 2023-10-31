#include <stdio.h>
#include <stdlib.h>

int funkcja(unsigned n, unsigned m)
{
    if(m==0)
    {
        return n;
    }
    else if(n==0)
    {
        return m;
    }
    else if (m > n)
    {
        int x = m;
        m = n;
        n = x;
    }

    int w = n - m + funkcja(n-1,m) + funkcja(n,m-1);
    return w;
}

int main()
{
    unsigned n,m;
    scanf("%u", &n);
    scanf("%u", &m);
    printf("%d", funkcja(n,m));


    return 0;
}
