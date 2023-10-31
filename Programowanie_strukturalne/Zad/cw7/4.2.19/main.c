#include <stdio.h>
#include <stdlib.h>


int *fun(unsigned n, int tab1[n])
{
    int l = 0;
    for(int i=0; i<n; i++)
    {
        if(tab1[i]!=0)
        {
            l+= 1;
        }
    }
    int * tab2 = malloc(l * sizeof(int));
    int x = 0;
    for(int i=0; i<n; i++)
    {
        if(tab1[i]!=0)
        {
            *(tab2+x) = tab1[i];
            x++;
        }
    }
    return tab2;
}

int main()
{
    int tab[5] = {5,0,6,7,0};
    int *y = fun(5, tab);
    printf("%p\n", y);
    printf("%d\n", *y);
    printf("%d\n", *(y+1));
    printf("%d\n", *(y+2));

    return 0;
}
