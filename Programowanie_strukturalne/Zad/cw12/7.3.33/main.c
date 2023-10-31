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

struct element * przesunbez(struct element *Lista)
{
    if(Lista==NULL)
    {
        return NULL;
    }
    if(Lista->next==NULL)
    {
        return Lista;
    }
    struct element *nowy = Lista;
    while(Lista->next->next!=NULL)
    {
        Lista = Lista->next;
    }
    Lista->next->next = nowy;
    nowy = Lista->next;
    Lista->next = NULL;
    return nowy;
}

void przesunz(struct element *Lista)
{
    struct element *nowy = Lista->next;
    struct element *nowy1 = Lista->next;
    int t=-1;
    while(Lista!=NULL)
    {
        t++;
        Lista = Lista->next;
    }
    int tab[t];
    int j=0;
    while(nowy!=NULL)
    {
        tab[j]= nowy->i;
        nowy = nowy->next;
        j++;
    }
    int k=0;
    nowy1->i=tab[t-1];
    while(nowy1->next!=NULL)
    {
        nowy1=nowy1->next;
        nowy1->i=tab[k];
        k++;
    }
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
    wyswietlbez(l);
    struct element * p = przesunbez(l);
    wyswietlbez(p);

    struct element* k = malloc(sizeof(struct element));  //z glowa
    k->next=malloc(sizeof(struct element));
    k->next->i=-9;
    k->next->next=malloc(sizeof(struct element));
    k->next->next->i=-8;
    k->next->next->next=malloc(sizeof(struct element));
    k->next->next->next->i=-5;
    k->next->next->next->next=NULL;
    wyswietlz(k);
    przesunz(k);
    wyswietlz(k);

    return 0;
}

