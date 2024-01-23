#include <stdio.h>
#include <stdlib.h>


struct element
{
    int i;
    struct element *next;
};


void wyswietlz(struct element *Lista)
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

void wyswietlbez(struct element *Lista)
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

struct element * kopiabez(struct element *Lista)
{
    struct element * wynik;
    struct element * temp;
    if(Lista==NULL)
    {
        return NULL;
    }
    wynik = malloc(sizeof(struct element));
    temp = wynik;
    temp->i = Lista->i;
    Lista = Lista->next;
    while(Lista!=NULL)
    {
        temp->next = malloc(sizeof(struct element));
        temp = temp->next;
        temp->i=Lista->i;
        Lista=Lista->next;
    }
    temp->next=NULL;
    return wynik;
}

struct element * kopiaz(struct element *Lista)
{
    struct element * wynik;
    struct element * temp;
    if(Lista->next==NULL)
    {
        return NULL;
    }
    wynik = malloc(sizeof(struct element));
    temp = wynik;
    temp->next = malloc(sizeof(struct element));
    temp = temp->next;
    Lista = Lista->next;
    temp->i = Lista->i;
    Lista = Lista->next;
    while(Lista!=NULL)
    {
        temp->next = malloc(sizeof(struct element));
        temp = temp->next;
        temp->i=Lista->i;
        Lista=Lista->next;
    }
    temp->next=NULL;
    return wynik;
}


int main()
{
    struct element * l=malloc(sizeof(struct element)); //bez
    l->i=-7;
    l->next=malloc(sizeof(struct element));
    l->next->i =5;
    l->next->next=malloc(sizeof(struct element));
    l->next->next->i=-8;
    l->next->next->next=NULL;
    struct element * p = kopiabez(l);
    wyswietlbez(l);
    wyswietlbez(p);

    struct element* k = malloc(sizeof(struct element));  //z g³owš
    k->next=malloc(sizeof(struct element));
    k->next->i=-9;
    k->next->next=malloc(sizeof(struct element));
    k->next->next->i=-8;
    k->next->next->next=malloc(sizeof(struct element));
    k->next->next->next->i=-5;
    k->next->next->next->next=NULL;
    struct element * m = kopiaz(k);
    wyswietlz(k);
    wyswietlz(m);

    return 0;
}
