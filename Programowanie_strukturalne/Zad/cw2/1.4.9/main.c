#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m;
    scanf("%d", &n);
    scanf("%d", &m);

    while (n!=m)
    {
        if(n>m)
        {
            n =n-m;
        }
        else
        {
            m =m-n;
        }
    }

    printf("%d", n);



    return 0;
}
