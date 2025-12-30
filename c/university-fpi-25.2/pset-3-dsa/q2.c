#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node{
  char value;
  struct Node* next;
} Node;

typedef struct {
  Node* head;
  Node* tail;
  int size;
} LinkedList;

void init_list(LinkedList* l);
void free_list(LinkedList* l);
void insert_begin(LinkedList* l, char v);
void insert_after(LinkedList* l, Node* current, char v);
void insert_end(LinkedList* l, char v);
void remove_value(LinkedList* l, char v);
void print_list(LinkedList* l);
bool is_empty(LinkedList* l);

int main(){
  LinkedList liststr;
  init_list(&liststr);
  
  char k;
  Node* current = NULL;
  bool beginning = false;
  while (scanf("%c", &k) != EOF){
    if (k == '[' || k == ']' || k == '\n'){
      if (k == '[') beginning = true;
      else if (k == ']') {
        beginning = false;
        current = liststr.tail;
      }
    }
    else{
      if (liststr.head == NULL){
        insert_begin(&liststr, k);
        current = liststr.head;
        beginning = false;
      }
      else if(beginning){
        insert_begin(&liststr, k);
        current = liststr.head;
        beginning = false;
      }
      else{
        insert_after(&liststr, current, k);
        current = current->next;
      }
    }
  }

  for (Node* ptr = liststr.head; ptr != NULL; ptr = ptr->next){
    printf("%c", ptr->value);
  }

  free_list(&liststr);
  return 0;
}

void init_list(LinkedList* l){
  l->head = NULL;
  l->tail = NULL;
  l->size = 0;
}

void insert_begin(LinkedList* l, char v){
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate. Exiting");
    exit(1);
  }
  new->value = v;
  new->next = l->head;
  l->head = new;

  if (l->tail == NULL) l->tail = new;
  
  l->size++;
}

void insert_after(LinkedList* l, Node* current, char v){
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate. Exiting");
    exit(1);
  }
  new->value = v;
  
  new->next = current->next;
  current->next = new;

  if (current == l->tail) l->tail = new;
  l->size++;
}

void insert_end(LinkedList* l, char v){ 
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate. Exiting");
    exit(1);
  }

  new->value = v;
  new->next = NULL;
  
  if (l->size == 0){
    l->head = new;
    l->tail = new;
  }
  else{
    l->tail->next = new;
    l->tail = new;
  }
  l->size++;
}

void remove_value(LinkedList* l, char v){
  if (l->size == 0) ;// Skips

  else if (v == l->head->value){
    Node* old_head = l->head;
    l->head = l->head->next;

    if (l->head == NULL) l->tail = NULL;

    free(old_head);
    l->size--;
  }
  else{
    Node* old = l->head;
    for (Node* atual = l->head->next; atual != NULL; atual = atual->next){
      if (atual->value == v){
        old->next = atual->next;
        if (atual == l->tail) l->tail = old;
        free(atual);
        l->size--;
        return;
      }
      else{
        old = atual;
      }
    }
  }
}

void print_list(LinkedList* l){
  for (Node* atual = l->head; atual != NULL; atual = atual->next){
    printf("%d\n", atual->value);
  }
}

bool is_empty(LinkedList* l){
  return l->size == 0;
}

void free_list(LinkedList* l){
  Node* old = NULL;
  for (Node* atual = l->head; atual != NULL; atual = atual->next){
    if (old != NULL) free(old);
    old = atual;
  }
  if (old != NULL) free(old);

  l->head = NULL;
  l->tail = NULL;
  l->size = 0;
}

