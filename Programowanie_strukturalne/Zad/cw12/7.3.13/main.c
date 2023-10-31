#include <stdio.h>
#include <stdlib.h>


struct element
{
    int i;
    struct element *next;
};

void wyswietl(struct element *Lista)
{
    struct element * nowy = Lista->next;
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

void dodajk(struct element*Lista, int a)
{
    struct element * nowy =  Lista;
    while(nowy->next!=NULL)
    {
        nowy=nowy->next;
    }
    nowy->next=malloc(sizeof(struct element));
    nowy=nowy->next;
    nowy->i=a;
    nowy->next=NULL;
};



int main()
{
    struct element* p=malloc(sizeof(struct element));
    p->next=malloc(sizeof(struct element));
    p->next->i=8;
    p->next->next=malloc(sizeof(struct element));
    p->next->next->i=7;
    p->next->next->next=malloc(sizeof(struct element));
    p->next->next->next->i=6;
    p->next->next->next->next=NULL;
    wyswietl(p);
    dodajk(p,25);
    wyswietl(p);
    return 0;
}
