#include <stdio.h>
#include <stdlib.h>

int main()
{
    float x1, x2, y1, y2, c1, c2, W, Wx, Wy;
    printf("Podaj x1:");
    scanf("%f", &x1);
    printf("Podaj x2:");
    scanf("%f", &x2);
    printf("Podaj y1:");
    scanf("%f", &y1);
    printf("Podaj y2:");
    scanf("%f", &y2);
    printf("Podaj c1:");
    scanf("%f", &c1);
    printf("Podaj c2:");
    scanf("%f", &c2);

     W = x1*y2 - x2*y1;
     Wx = c1*y2 - c2*y1;
     Wy = x1*c2 - x2*c1;

    float x = Wx / W;
    float y = Wy / W;

    printf("%f \n%f \n%f\n", W,Wx,Wy);


    if ( W !=0)
    {
        printf("x = %f \ny = %f", x, y);
    }
    else if ( W == 0 && Wx == 0 && Wy == 0)
    {
        printf("Uk³ad ma nieskoñczon¹ liczbê rozwi¹zañ");
    }
    else
    {
        printf("Uk³ad nie ma rozwi¹zañ");
    }

    return 0;
}
