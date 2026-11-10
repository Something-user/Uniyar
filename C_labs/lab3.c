#include <stdio.h>
#include <stdlib.h>


typedef struct
{
    int id;
    int course;
    double score;
} Student;

typedef struct DNode
{
    struct DNode *prev;
    Student data;
    struct DNode *next;
} DNode;

typedef struct
{
    DNode *head;
    DNode *tail;
} DList;


DNode *make_node(Student s); /* Создание узла списка */
DNode *list_init(FILE *in, DList *list, int n); /*  */
void free_list(DNode *head); /* Функция очистки паямти */

int main()
{
    printf("Hello World!\n");
    return 0;
}


DNode *make_node(Student s)
{
    DNode *node = malloc(sizeof(*node));
    if(node == NULL){
        return NULL;
    }
    node->data = s;
    node->prev = NULL;
    node->next = NULL;
    return node;
}


DNode *list_init(FILE *in, DList *list, int n)
{
    DNode *head = NULL;
    DNode *tail = NULL;

    for(int i = 0; i < n; i++){
        Student s;
        if(fscanf(in, "%d %d %lf", &s.id, &s.course, &s.score) != 3){
            free_list(head);
            return NULL;
        }

        DNode *node = make_node(s);
        if(node == NULL){
            free_list(head);
            return NULL;
        }

        node->data = s;
        node->prev = NULL;
        node->next = NULL;

        if(tail == NULL)
        {
            head = tail = node;
        }
        else
        {
            node->prev = tail;
            tail->next = node;

            tail = node;
        }
    }
    return head;
}

void free_list(DNode *head)
{
    DNode *p = head;
    while(p != NULL)
    {
        DNode *next = p->next;
        free(p);
        p = next;
    }
    head = NULL;
}
