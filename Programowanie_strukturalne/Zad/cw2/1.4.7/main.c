#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m;
    scanf("%d", &n);
    scanf("%d", &m);
    if(n >= m)
    {
        printf("n musi byæ mniejsze od m \n");
    }
    else
    {
        int iloczyn = 1;
        for(int i = n; i <= m; i++)
        {
            iloczyn *= i;
        }
        printf("%d", iloczyn);
    }

    return 0;
}
