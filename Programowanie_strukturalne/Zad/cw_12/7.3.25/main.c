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

int minimumbez(struct element *Lista)
{
    int wynik = Lista->i;
    while(Lista!=NULL)
    {
        if(Lista->i<wynik)
        {
            wynik=Lista->i;
        }
        Lista= Lista->next;
    }
    return wynik;
}

int minimumz(struct element *Lista)
{
    int wynik = Lista->next->i;
    while(Lista->next!=NULL)
    {
        Lista= Lista->next;
        if(Lista->i<wynik)
        {
            wynik=Lista->i;
        }

    }
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
    wyswietlbez(l);
    printf("%d\n\n", minimumbez(l));

    struct element* p = malloc(sizeof(struct element));  //z g³owš
    p->next=malloc(sizeof(struct element));
    p->next->i=-9;
    p->next->next=malloc(sizeof(struct element));
    p->next->next->i=-8;
    p->next->next->next=malloc(sizeof(struct element));
    p->next->next->next->i=-5;
    p->next->next->next->next=NULL;
    wyswietlz(p);
    printf("%d\n\n", minimumz(p));

    return 0;
}
