#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM_MAXIMO 500

char** inicializar_vetor_strings(int* qtd_strings);

void alocar_string_ao_vetor(size_t tam_string, int qtd_strings, char*** m_str_ptr);

void desalocar_vetor_strings(char** vet, int qtd);

int main(){
  char** str = NULL;
  int linhas = 0;
  str = inicializar_vetor_strings(&linhas);
  
  desalocar_vetor_strings(str, linhas);
  return 0;
}

char** inicializar_vetor_strings(int* qtd_strings){
  int tam_string = 0;
  char auxStr[TAM_MAXIMO];
  
  char** m = NULL;
   
  while(scanf(" %499s", auxStr) != EOF){
    ++(*qtd_strings);
    
    tam_string = strlen(auxStr);

    alocar_string_ao_vetor(tam_string, *qtd_strings, &m);
    strcpy(m[*qtd_strings - 1], auxStr);

    tam_string = 0;
  }

  return m;
}

void alocar_string_ao_vetor(size_t tam_string, int qtd_strings, char*** m_str_ptr){

  char** aux_ptr = NULL;
  aux_ptr = realloc(*m_str_ptr, sizeof(char*) * qtd_strings);
  if (aux_ptr == NULL){
    desalocar_vetor_strings(*m_str_ptr, qtd_strings - 1);
    exit(1);
  }
  *m_str_ptr = aux_ptr;
  (*m_str_ptr)[qtd_strings - 1] = malloc(tam_string + 1);
  if ((*m_str_ptr)[qtd_strings-1] == NULL){
    desalocar_vetor_strings(*m_str_ptr, qtd_strings - 1);
    exit(1);
  }
}

void desalocar_vetor_strings(char** vet, int qtd_strings){
  
  for (int i = 0; i < qtd_strings; i++){
    free(vet[i]);
  }
  free(vet);
}

