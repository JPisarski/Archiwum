#include <stdio.h>
#include <stdlib.h>


int suma = 0;


void liczbawywolan(void)
{
    suma +=1;
    printf("%d\n", suma);
}


int main()
{
    liczbawywolan();
    liczbawywolan();
    liczbawywolan();

    return 0;
}
