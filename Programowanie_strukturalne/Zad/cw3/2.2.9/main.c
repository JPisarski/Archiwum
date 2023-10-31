#include <stdio.h>
#include <stdlib.h>


float pierwiastek(int m, unsigned n)
{
    float w = pow(n,(1./m));
    w = (int)w;
    return w;
}


int main()
{
    int m;
    unsigned n;
    scanf("%d", &m);
    scanf("%u", &n);
    printf("%f", pierwiastek(m,n));

    return 0;
}
