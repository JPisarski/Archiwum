#include <stdio.h>
#include <stdlib.h>

int main()
{
   printf("Wybierz figur�:\n1 - kwadrat \n2 - prostok�t \n3 -tr�jk�t\n");
   int x;
   scanf("%d", &x);

   float x1,x2,x3;


   if (x == 1 || x == 2)
   {

       scanf("%f", &x1);
       scanf("%f", &x2);

       float P = x1 * x2;
       printf("Pole figury wynosi: %f", P);
   }
   else if (x == 3)
   {
       scanf("%f", &x1);
       scanf("%f", &x2);
       scanf("%f", &x3);

       float p = (x1 + x2 + x3)/2;
       float P = sqrtf(p*(p-x1)*(p-x2)*(p-x3));
       printf("Pole figury wynosi: %f", P);
   }

    return 0;
}
