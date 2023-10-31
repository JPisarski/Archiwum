#include <stdio.h>
#include <stdlib.h>


void przypadeka(unsigned x)
{
    for(int i=1; i<x; i++)
    {
        for(int j=1; j<x; j++)
        {
            if(i*i+j*j==x)
            {
                printf("(%d^2)+(%d^2)=%d\n", i,j,x);
            }
        }
    }
}

void przypadekb(unsigned x)
{
     for(int i=1; i<x; i++)
    {
        for(int j=1; j<i; j++)
        {
            if(i*i+j*j==x)
            {
                printf("(%d^2)+(%d^2)=%d\n", i,j,x);
            }
        }
    }
}

int main()
{
    unsigned n;
    scanf("%d", &n);
    przypadeka(n);
    printf("\n");
    przypadekb(n);


    return 0;
}
