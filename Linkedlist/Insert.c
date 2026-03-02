#include <stdio.h>
#include <stdlib.h>

// Create Struct data type.
struct Node
{
    int data;
    struct Node *next;
};

// function for traversal
void traversal(struct Node *ptr)
{
    while(ptr != NULL)
    {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
}

void InsertAtFirst(struct Node **head, int value)
{
    struct Node *new;
    new=(struct Node*)malloc(sizeof(struct Node));
    new -> data= value;
    new -> next= *head;
    *head =new;
}

int main()
{
    // Struct Node data type name.
    struct Node *head;
    struct Node *second;
    struct Node *third;

    // allocate memory for them.
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));

    // giving them value.
    head->data = 12;
    head->next = second;
    second->data = 32;
    second->next = third;
    third->data = 55;
    third->next = NULL;

    // Get user input and insert at beginning
    int v;
    printf("Enter value to insert:");
    scanf("%d",&v);

    InsertAtFirst(&head,v);
    traversal(head);

    return 0;
}