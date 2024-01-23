#include <stdio.h>
#include <stdlib.h>


struct element
{
    int i;
    struct element *next;
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

struct element* stworz()
{
    return NULL;
};

struct element* usunw(struct element* Lista, struct element* Elem)
{

    struct element * nowy1;
    struct element * nowy2;
    if(Lista==NULL)
    {
        return Lista;
    }
    nowy1=Lista;
    if(Lista==Elem)
    {
        Lista=Lista->next;
        free(nowy1);
        return Lista;
    }
    else
    {
        while((nowy1->next!=NULL)&&(nowy1->next!=Elem))
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
    return Lista;
};
int main()
{
    struct element * p=malloc(sizeof(struct element));
    p->i=7;
    p->next=malloc(sizeof(struct element));
    p->next->i =5;
    p->next->next=malloc(sizeof(struct element));
    p->next->next->i=8;
    p->next->next->next=NULL;
    struct element * l = p;
    wyswietl(p);
    p = usunw(p,l);
    wyswietl(p);
    return 0;
}
