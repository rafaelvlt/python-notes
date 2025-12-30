#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int fatorarInteiro(long long num);

char* pegarFrase(unsigned long* tam_frase);

void cifra(char* frase, int chave);

int main(){
  long long num;
  scanf("%lld", &num);
  getchar(); // limpa \n
  
  int qtd_fatores = fatorarInteiro(num);

  char* frase = NULL;
  unsigned long tam_frase = 0;
  frase = pegarFrase(&tam_frase);  
  
  cifra(frase, qtd_fatores);

  printf("%d\n%s", qtd_fatores, frase);

  free(frase);

  return 0;
}

void realocarLista(int** lista_original_ptr, int tamanho){
  
  int* paux = realloc(*lista_original_ptr, sizeof(int) * (tamanho + 1));
  if (paux == NULL){
    free(*lista_original_ptr);
    exit(1);
  }
  *lista_original_ptr = paux;
}

int fatorarInteiro(long long num){

  if (num <= 1) return 0;
  
  int qtd = 0;
  int* listaDiv = malloc(sizeof(int) * (qtd+1));

  while (num % 2 == 0) {
    listaDiv[qtd] = 2; 
    qtd++;
    num /= 2;
    realocarLista(&listaDiv, qtd);
  }

  for (unsigned long i = 3; i * i <= num; i += 2) {
    while (num % i == 0) {
      listaDiv[qtd] = i;
      qtd++;
      num /= i;
      realocarLista(&listaDiv, qtd);
    }
  }

  if (num > 2) {
    qtd++;
  }

  free(listaDiv);

  return qtd;
}

char* pegarFrase(unsigned long* tam_frase){

  unsigned long tam_atual = 100;
  unsigned long len = 0;
  
  char* temp = (char*) malloc(tam_atual + 1);
  if (temp == NULL) exit(1);
  char b;

  while((b = getchar()) != EOF && b != '\n'){
    temp[len] = b;
    len++;

    if (len == tam_atual){
      tam_atual *= 2;
      char* pAux = realloc(temp, tam_atual + 1);
      if (pAux == NULL){
        free(temp);
        exit(1);
      }
      temp = pAux;
    }
  }
  temp[len] = '\0';
  
  *tam_frase = len;
  
  return temp;
}


void cifra(char* frase, int chave){ 

  int incremento_pa = 0;
  
  for (int i = 0; frase[i] != '\0'; i++){
    if (isalpha((frase[i]))){
      int deslocamento = chave + incremento_pa;
      
      char casing;
      if (isupper(frase[i])) casing = 'A';
      else casing = 'a';

      frase[i] = casing + (frase[i] - casing + deslocamento) % 26;

      incremento_pa++;
    }
  }
}
