#include <stdio.h>
#include <stdlib.h>


struct element
{
    int i;
    struct element *next;
};

struct element * dodajk(struct element *Lista, int a)
{
    struct element * nowy ;
    if(Lista==NULL)
    {
        nowy=malloc(sizeof(struct element));
        Lista=nowy;
    }
    else
    {
        nowy=Lista;
        while(nowy->next!=NULL)
        {
            nowy=nowy->next;
        }
        nowy->next=malloc(sizeof(struct element));
        nowy=nowy->next;
    }
    nowy->i=a;
    nowy->next=NULL;
    return Lista;
}

struct element* stworz()
{
    return NULL;
};

void wyswietl(struct element *Lista)
{
    struct element * nowy = Lista;
    if(nowy == NULL)
    {
        printf("Lista jest pusta\n");
    }
    while(nowy != NULL)
    {
        printf("%d\n", nowy->i);
        nowy = nowy->next;
    }
    printf("----\n");
}



int main()
{
    struct element *p = stworz();
    p = dodajk(p, 5);
    p = dodajk(p, 6);
    p = dodajk(p, 7);
    p = dodajk(p, 8);
    p = dodajk(p, 9);
    wyswietl(p);
    return 0;
}
