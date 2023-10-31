#include <stdio.h>
#include <stdlib.h>
struct punktn
{
    int wymiar;
    int *punkt;
};
void przepisz(struct punktn tab1[],struct punktn tab2[], int n)
{
    for(int i=0;i<n;i++)
    {
        tab2[i].wymiar = tab1[i].wymiar;
        tab2[i].punkt = malloc(tab2[i].wymiar*sizeof(int));
        for(int j=0; j<tab1[i].wymiar; j++)
        {
            tab2[i].punkt[j] = tab1[i].punkt[j];
        }
    }
}
void wyswietlp(struct punktn x)
{
    for(int i=0; i<x.wymiar; i++)
    {
        printf("%d ", x.punkt[i]);
    }
    printf("\n");
}
void wyswietlt(struct punktn tab[], int n)
{
    for(int i=0;i<n;i++)
    {
        wyswietlp(tab[i]);
    }
}
int main()
{
    struct punktn punkt1;
    punkt1.wymiar = 2;
    punkt1.punkt = malloc(punkt1.wymiar*sizeof(int));
    punkt1.punkt[0] = 6;
    punkt1.punkt[1] = 5;
    struct punktn punkt2;
    punkt2.wymiar = 2;
    punkt2.punkt = malloc(punkt2.wymiar*sizeof(int));
    punkt2.punkt[0]=7;
    punkt2.punkt[1]=8;
    struct punktn tab1[2]={punkt1, punkt2};
    wyswietlt(tab1,2);
    struct punktn tab2[2];
    przepisz(tab1, tab2, 2);
    wyswietlt(tab2 ,2);
    return 0;
}
