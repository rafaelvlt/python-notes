#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

typedef struct{
  int* items;
  int numElems;
  int capacity;
} Pilha;

void initStack(Pilha* p, int capacity);
bool isEmpty(Pilha* p);
void push(Pilha* p, int v);
int pop(Pilha* p);
int top(Pilha* p);
void freeStack(Pilha* p);

void solve(){
  static int num_pilha = 0;
  num_pilha++;

  Pilha p;
  initStack(&p, 10);
  int v = 0;
  scanf("%d", &v);
  while(v != 0){
    push(&p, v);
    scanf("%d", &v);
  }
  if (p.numElems == -1){
    printf("Pilha %d: 0 -1\n", num_pilha);
  }
  else{
    printf("Pilha %d: %d %d\n", num_pilha, p.numElems + 1, top(&p));
  }
  freeStack(&p);
}

int main(){
  int t = 0;
  scanf("%d", &t);
  while (t--){ 
    solve();
  }
  return 0;
}

void initStack(Pilha* p, int capacity){
  p->items = (int *) malloc(sizeof(int) * capacity);
  if (p->items == NULL){
    printf("Initialization error\n");
    exit(1);
  }
  p->numElems = -1;
  p->capacity = capacity;
}

bool isEmpty(Pilha* p){
  return (p->numElems == -1);
}

int top(Pilha* p){
  if (!isEmpty(p)){
    return p->items[p->numElems];
  }
  else{
    printf("Stack is empty.\n");
    return -1;
  }
}

void push(Pilha* p, int v){
  if (p->numElems == p->capacity - 1){
    p->capacity *= 2;
    p->items = (int *)realloc(p->items, p->capacity * sizeof(int));
    if (p == NULL){
      printf("Memory allocation failed!\n");
      freeStack(p);
      exit(1);
    }
  }
  if (v != 0){
    p->items[++(p->numElems)] = v;
    if (p->numElems >= 1){
      int prev = p->items[p->numElems - 1];
      if ((v % 2 != 0) && (prev % 2 != 0)){
        pop(p);
        pop(p);
        push(p, abs(v - prev));
      }
      else if ((v % 2 == 0) && (prev % 2) == 0){
        pop(p);
        pop(p);
        push(p, abs(v - prev));
      }
    }
  }
}


int pop(Pilha* p){
  if (isEmpty(p)){
    printf("Stack underflow.\n");
    return -1;
  }
  else{
    return p->items[(p->numElems)--];
  }
}

void freeStack(Pilha* p){
  free(p->items);
}

