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

void usun(struct element* Lista, int a)
{
    struct element* nowy1=Lista;
    struct element* nowy2;
    while((nowy1->next!=NULL)&&(nowy1->next->i!=a))
    {
        nowy1=nowy1->next;
    }
    if(nowy1->next!=NULL)
    {
        nowy2=nowy1->next;
        nowy1->next=nowy2->next;
        free(nowy2);
    }
}


int main()
{
    struct element* p = malloc(sizeof(struct element));
    p->next=malloc(sizeof(struct element));
    p->next->i=9;
    p->next->next=malloc(sizeof(struct element));
    p->next->next->i=8;
    p->next->next->next=malloc(sizeof(struct element));
    p->next->next->next->i=5;
    p->next->next->next->next=NULL;
    wyswietl(p);
    usun(p,8);
    wyswietl(p);

    return 0;
}
