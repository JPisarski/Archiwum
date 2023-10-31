#include <stdio.h>
#include <stdlib.h>

   funkcja(int const *x, int * y)
   {
       *y = *x;
   }

int main()
{
   int const x;
   int y;
   scanf("%d", &x);
   scanf("%d", &y);
   funkcja(&x, &y);
   printf("%d, %d\n", x, y);
   return 0;
}
