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

typedef enum
{
    MEMORY_ERROR = 1, FILE_ERRROR
} errors;


DNode *make_node(Student s); /* Создание узла списка */
void make_list(DList *list); /* Функция создания и очистки списка */
void list_init(FILE *in, int n, DList *list); /* Функция считывания списка из файла */
void free_list(DList *list); /* Функция очистки паямти */
void print_list(FILE *out, const DNode *head); /* Функция вывода обработанного списка в файл */

int main()
{
    FILE *in = fopen("input.txt", "r");
    if(in == NULL){
        perror("input.txt");
        return 1;
    }

    int n = 0;
    fscanf(in, "%d", &n);

/*
    if(fscanf(in, "%d", &n) != 1){
        if(fclose(in) != 0){
            return 1;
        }
        return 1;
        
    }
*/

    DList list;
    list_init(in, n, &list);

    if(fclose(in) != 0)
    {
        free_list(&list);
        return 1;
    }
    



    FILE *out = fopen("output.txt", "w");
    if(out == NULL){
        perror("output.txt");
        free_list(&list);
        return 1;
    }

    print_list(out, list.head);

    if(fclose(out) != 0){
        free_list(&list);
        return 1;
    }

    free_list(&list);
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

void make_list(DList *list)
{
    list->head = NULL;
    list->tail = NULL;
}


void list_init(FILE *in, int n, DList *list)
{
    //DNode *head = NULL;
    //DNode *tail = NULL;
    
    make_list(list);

    for(int i = 0; i < n; i++){
        Student s;
        if(fscanf(in, "%d %d %lf", &s.id, &s.course, &s.score) != 3){
            free_list(list);
            make_list(list);
            return;
        }

        DNode *node = make_node(s);
        if(node == NULL){
            free_list(list);
            make_list(list);
            return;
        }

        node->data = s;
        node->prev = NULL;
        node->next = NULL;

        if(list->tail == NULL)
        {
            list->head = list->tail = node;
        }
        else
        {
            node->prev = list->tail;
            list->tail->next = node;

            list->tail = node;
        }
    }
}

void free_list(DList *list)
{
    DNode *p = list->head;
    while(p != NULL)
    {
        DNode *next = p->next;
        free(p);
        p = next;
    }
    make_list(list);
}

DNode *swap(int n, DList *list)
{
    if(n % 2){
        DNode *node = list->head;
        for(int i = 0; i < n/2; i++){
            node = node->next;
            node = node->prev;
        }
        
        //DNode *cur = node;
    }
}


void print_list(FILE *out, const DNode *head)
{
    for (const DNode *p = head; p != NULL; p = p->next)
    {
        fprintf(out ,"%d %d %.2f\n", p->data.id, p->data.course, p->data.score);
    }
}
