#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct Node{
  int value;
  char nome[10];
  struct Node* next;
  struct Node* prev;
} Node;

typedef struct {
  Node* head;
  Node* tail;
  int size;
} LinkedList;

void init_list(LinkedList* l);
void free_list(LinkedList* l);
void insert_begin(LinkedList* l, int v, char nome[10]);
void insert_after(LinkedList* l, Node* current, int v, char nome[10]);
void insert_end(LinkedList* l, int v, char nome[10]);
void remove_value(LinkedList* l, int v);
void print_list(LinkedList* l);
bool is_empty(LinkedList* l);
bool procurar(LinkedList* l, char nome[10]){
  for (Node* current = l->head; current != NULL; current = current->next){
    if (strcmp(nome, current->nome) == 0){
      return true;
    }
  }
  return false;
}


int main(){
  int K;
  scanf("%d", &K);
  getchar(); //tirar \n
  char buff[256];

  LinkedList l;
  init_list(&l);

  for (int i = 0; i < K; i++){
    fgets(buff, sizeof(buff), stdin);
    char comando[5];
    sscanf(buff, "%s", comando);
    if (strcmp(comando,"ADD") == 0){
      char nome[10];
      int pontos;
      sscanf(buff, "%s %s %d", comando, nome, &pontos);
      bool check = procurar(&l, nome);
      if (check){
        printf("%s ja esta no sistema.\n", nome);
      }
      else{
        if (l.head == NULL || pontos < l.head->value){
          insert_begin(&l, pontos, nome);
        } 
        else{
          Node* search = l.head;
          while (search->next != NULL && search->next->value < pontos){
            search = search->next;
          }
          insert_after(&l, search, pontos, nome);
        }
        printf("%s inserido com sucesso!\n", nome);
      }
    }
    else if (strcmp(comando,"PROX") == 0){
      int pontos;
      sscanf(buff, "%s %d", comando, &pontos);
      bool found = false;
      for (Node* current = l.head; current != NULL && !found; current = current->next){
        if (current->value == pontos){
          if (current->prev == NULL && current->next == NULL){
            printf("Apenas %s existe no sistema...\n", current->nome);
          }
          else if(current->prev == NULL && current->next != NULL){
            printf("%s e o menor! e logo apos vem %s\n", current->nome, current->next->nome);
          }
          else if(current->prev != NULL && current->next == NULL){
            printf("%s e o maior! e logo atras vem %s\n", current->nome, current->prev->nome);
          }
          else{
            printf("%s vem apos %s e antes de %s\n", current->nome, current->prev->nome, current->next->nome);
          }
        }
      }
    }
  }

  free_list(&l);
  return 0;
}

void init_list(LinkedList* l){
  l->head = NULL;
  l->tail = NULL;
  l->size = 0;
}

void insert_begin(LinkedList* l, int v, char nome[10]){
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate. Exiting");
    exit(1);
  }
  new->value = v;
  strcpy(new->nome, nome);
  new->next = l->head;
  new->prev = NULL;
  if (l->head != NULL) l->head->prev = new;
  l->head = new;

  if (l->tail == NULL) l->tail = new;
  
  l->size++;
}

void insert_after(LinkedList* l, Node* current, int v, char nome[10]){
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate. Exiting");
    exit(1);
  }
  new->value = v;
  strcpy(new->nome, nome);
  
  new->next = current->next;
  new->prev = current;
  if (current->next != NULL){
    current->next->prev = new;
  }
  current->next = new;

  if (current == l->tail) l->tail = new;
  l->size++;
}

void insert_end(LinkedList* l, int v, char nome[10]){ 
  Node* new = (Node*)malloc(sizeof(Node));
  if (new == NULL){
    printf("Failed to allocate. Exiting");
    exit(1);
  }

  new->value = v;
  strcpy(new->nome, nome);
  new->next = NULL;
  new->prev = l->tail;
  
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

void remove_value(LinkedList* l, int v){
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

