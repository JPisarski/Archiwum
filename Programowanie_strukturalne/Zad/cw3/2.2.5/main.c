#include <stdio.h>
#include <stdlib.h>

float potega(int x)
{
    float w = pow(2,x);
    return w;
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%f", potega(n));



    return 0;
}
