#include <stdio.h>
#include <stdlib.h>
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

void inverter_pilha(Pilha* p, Pilha* inversa){ 
  initStack(inversa, p->numElems);
  for (int i = 0; i <= p->numElems; i++){
    push(inversa, p->items[p->numElems-i]);
  }
  freeStack(p);
}

void pares_negativos(Pilha* p){
  for (int i = 0; i <= p->numElems; i++){
    if (p->items[i] % 2 == 0) p->items[i] = -(p->items[i]);
  }
}

void anular_repetidas(Pilha* p){
  for (int i = p->numElems; i >= 0; i -= 2){
    if ((i - 1) >= 0){
      if (p->items[i] == p->items[i-1]){
        pop(p);
        pop(p);
      }
      else{
        return ;
      }
    }
    else{
      return ; 
    }
  }
}

int soma_dano(Pilha* p){
  int dano = 0;
  for (int i = p->numElems; i >= 0; i--) dano += p->items[i];
  return dano;
}

void printar_pilha(Pilha* p){
  for (int i = p->numElems; i >= 0; i--) printf("%d ", p->items[i]);
  printf("\n");
}

int main(){
  int vida_vecna = 0;
  int tam_pilha = 0;
  scanf("%d %d", &vida_vecna, &tam_pilha);

  Pilha ataques_inicial;
  initStack(&ataques_inicial, tam_pilha);
  for (int i = 0; i < tam_pilha; i++){
    int ataque = 0;
    scanf("%d", &ataque);
    push(&ataques_inicial, ataque);
  }
  printar_pilha(&ataques_inicial);

  Pilha ataques_final;
  inverter_pilha(&ataques_inicial, &ataques_final);
  pares_negativos(&ataques_final);
  anular_repetidas(&ataques_final);
  printar_pilha(&ataques_final);
  int dano_total = soma_dano(&ataques_final);
  
  if (dano_total >= vida_vecna){
    printf("Atravessou o Mundo Invertido com %d pontos. Vecna foi derrotado!", dano_total);
  }
  else{
    printf("Atravessou o Mundo Invertido com %d pontos. Hawkins esta condenada...", dano_total);
  }
  
  freeStack(&ataques_final);
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
  p->items[++(p->numElems)] = v;
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

