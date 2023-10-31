#include <stdio.h>
#include <stdlib.h>


 void fun(int (*wsk)(int a, int b), int n)
 {
     int x = wsk(n, n);
     printf("%d\n", x);
 }

 int suma(int a, int b)
 {
     return a + b;
 }

int main()
{
    fun(suma, 15);
    return 0;
}
