#include <stdio.h>
#include <stdlib.h>

int main()
{
   int x,y;


   scanf("%d", &x);
   scanf("%d", &y);

   if (abs(x) > abs(y))
   {
       printf("%d", x);
   }
   else if (abs(y) > abs(x))
   {
       printf("%d", y);
   }


    return 0;
}
