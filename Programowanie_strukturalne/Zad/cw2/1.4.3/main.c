#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m,k;
    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%d", &k);

    for(int i=1; i*n < k ; i++)
    {
        int x = i*n;
        if (x <= m)
        {
            continue;
        }

        printf("%d \n", x);
    }

    return 0;
}
