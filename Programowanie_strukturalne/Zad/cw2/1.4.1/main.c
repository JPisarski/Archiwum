#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m;
    scanf("%d", &n);
    scanf("%d", &m);

    for(int i=1; i*n < m; i++)
    {
        int x = i*n;

        printf("%d \n", x);
    }
    return 0;
}
