#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFF_SIZE 10000
#define TAM_PESQUISADOR 100
#define TAM_TITULO 300

typedef enum {
  Mestre,
  Doutor,
} Titulo;

typedef struct{
  char nome[TAM_PESQUISADOR];
  Titulo titulacao;
} Pesquisador;

typedef struct {
  int codigo;
  char titulo[TAM_TITULO];
  float orcamento;
  Pesquisador* participantes;
  int num_participantes;
} Projeto;

Projeto* carregarProjetos(const char* nomeArquivo, int* numProjetos);

void adicionarProjeto(Projeto** projetos, int* numProjetos);

void adicionarPesquisador(Projeto* projetos, int numProjetos);

void gerarRelatorio(const char* nomeArquivo, Projeto* projetos, int numProjetos);

void liberarMemoria(Projeto* projetos, int numProjetos);

int main(){
    
  Projeto* listaProjetos = NULL;
  int numProjetos = 0;
  listaProjetos = carregarProjetos("projetos.txt", &numProjetos);

  adicionarProjeto(&listaProjetos, &numProjetos);
  adicionarPesquisador(listaProjetos, numProjetos);
  liberarMemoria(listaProjetos, numProjetos);

  return 0;
}

Projeto* carregarProjetos(const char* nomeArquivo, int* numProjetos){
  // Abre arquivo para leitura
  FILE* arquivo = fopen(nomeArquivo, "r");
  if (arquivo == NULL){
    exit(1);
  }
  printf("Lendo %s...\n", nomeArquivo);
  
  //define capacidade inicial, caso tenha necessidade(chegar a ela) é reallocado
  int capacidade_proj = 10;
  Projeto* templista = (Projeto*) malloc(sizeof(Projeto) * capacidade_proj);
  int n = 0;

  char buffer[MAX_BUFF_SIZE];
  //da parse no projeto linha a linha
  while(fgets(buffer, sizeof(buffer), arquivo) != NULL){
    //codigo
    sscanf(buffer, "Codigo: %d", &templista[n].codigo);
    printf("codigo: %d\n", templista[n].codigo);
    //Titulo
    fgets(buffer, sizeof(buffer), arquivo);
    buffer[strcspn(buffer, "\n")] = '\0';
    sscanf(buffer, "Titulo: %99[^\n]", templista[n].titulo);
    printf("Titulo: %s\n", templista[n].titulo);

    //Orçamento
    fgets(buffer, sizeof(buffer), arquivo);
    sscanf(buffer, "Orcamento: %f", &templista[n].orcamento);
    printf("orcamento: %f\n", templista[n].orcamento);

    //Pesquisadores
    fgets(buffer, sizeof(buffer), arquivo);
    sscanf(buffer, "Pesquisadores: %9999[^\n]", buffer);
    int lenb = strlen(buffer);

    //aloca memoria inicialmente para 1 pesquisador
    templista[n].num_participantes = 1;
    templista[n].participantes = malloc(sizeof(Pesquisador) * templista[n].num_participantes);

    // Loop itera para cada pesquisador, dando parse no texto do buffer para pegar os dados relevantes
    while(buffer[0] != '\0'){
      char tempnome[TAM_PESQUISADOR];
      char strtitulo[10];
      
      //pega o nome do primeiro participante que achar da lista de projetos
      sscanf(buffer, "%[^(]", templista[n].participantes[templista[n].num_participantes-1].nome);


      // pega titulo em str
      int bufflen = strlen(buffer);
      int entrou_parenteses = 0;
      int titulo_idx = 0;
      for(int i = 0; buffer[i] != ')'; i++){
        if (entrou_parenteses){
          strtitulo[titulo_idx] = buffer[i];
          titulo_idx++;
        }

        if (buffer[i] == '('){
          entrou_parenteses = 1;
        }
      }

      // debug printf("strtitulo: %s\n", strtitulo);

      //converte a titulacao em enum
      if (strcmp(strtitulo, "Mestre") == 0) templista[n].participantes[templista[n].num_participantes-1].titulacao = Mestre;
      else templista[n].participantes[templista[n].num_participantes-1].titulacao = Doutor;

      // debug printf("buffer_pesquisador: %s\n", buffer);
      printf("nome_pesquisador: %s\n", templista[n].participantes[templista[n].num_participantes-1].nome);
      printf("titulo_pesquisador: %d\n", templista[n].participantes[templista[n].num_participantes-1].titulacao);

      //serve para deletar a linha de pesquisadores até o inicio do proximo
      char tempbuffer[MAX_BUFF_SIZE];
      int newbuffidx = 0;
      int bufferlen = strlen(buffer);
      int achouvirg = 0;
      int pularespaco = -1;
      for (int i = 0; i < bufferlen; i++){
        if (buffer[i] == ',' ) achouvirg = 1;
        if (achouvirg){
            if(pularespaco > 0){
                tempbuffer[newbuffidx] = buffer[i];
                newbuffidx++;
            }
            pularespaco++;
          } 
        }
      tempbuffer[newbuffidx] = '\0';
      strcpy(buffer, tempbuffer);

      //se tiver mais pesquisadores, dá realloc
      if (buffer[0] != '\0'){
        templista[n].num_participantes++;
        Pesquisador* paux = realloc(templista[n].participantes, sizeof(Pesquisador) * templista[n].num_participantes);
        if (paux == NULL){
            perror("Erro ao realocar pesquisadores de um projeto");
            free(templista[n].participantes);
            exit(1);
        }
        templista[n].participantes = paux;
      }
    }
    //tira os hifens entre os projetos
    fgets(buffer, sizeof(buffer), arquivo);
    n++;
    printf("\n");

    /* debug
    for (int i = 0; i < templista[n].num_participantes; i++){
        printf("nome: %s  titutalacao: %d\n", templista[n].participantes[i].nome);
    }
    break;
    */
  }
  fclose(arquivo);
  *numProjetos = n;
  return templista;
}

void adicionarProjeto(Projeto** projetos, int* numProjetos){

  //Adiciona ao fim da lista de projetos
  (*numProjetos)++;
  int projetoidx = *numProjetos - 1;
  Projeto* paux = realloc(*projetos, sizeof(Projeto) * *numProjetos);
  if (paux == NULL){
    perror("Erro ao realocar lista de projetos ao adicionar projeto");
    free(*projetos);
    exit(1);
  }
  *projetos = paux;

  printf("Digite o código do projeto: ");
  scanf("%d", &(*projetos)[projetoidx].codigo);
  printf("Digite o título do projeto: ");

  getchar(); //limpa buffer
  fgets((*projetos)[projetoidx].titulo, sizeof((*projetos)[projetoidx].titulo), stdin);
  printf("Digite o orçamento: ");
  scanf("%f", &(*projetos)[projetoidx].orcamento);

  printf("Digite o numero de participantes: ");
  scanf("%d", &(*projetos)[projetoidx].num_participantes);
  getchar(); //limpa buffer
  (*projetos)[projetoidx].participantes = malloc(sizeof(Pesquisador) * (*projetos)[projetoidx].num_participantes);
  
  //loop pega nome do participante e nome do titulo e converte pro enum, adicionando ao fim da lista de projetos
  for (int i = 0; i < (*projetos)[projetoidx].num_participantes; i++){
    printf("Digite o nome do #%d participante: ", i+1);
    fgets((*projetos)[projetoidx].participantes[i].nome, sizeof((*projetos)[projetoidx].participantes[i].nome), stdin);

    printf("Digite o título do #%d participante(Doutor/Mestre): ", i+1);
    char (temptit)[TAM_TITULO];
    fgets(temptit, sizeof(temptit), stdin);
    
    if (strcmp(temptit, "Mestre") == 0) (*projetos)[projetoidx].participantes[i].titulacao = Mestre;
    else (*projetos)[projetoidx].participantes[i].titulacao = Doutor;
  }
  

}

void adicionarPesquisador(Projeto* projetos, int numProjetos){
  printf("Digite o código do projeto que deseja adicionar o pesquisador: ");
  int codigo;
  scanf("%d", &codigo);

  //acha o projeto pelo código e pega o idx dele
  int idxproj = 0;
  for (int i = 0; i < numProjetos; i++){
    if (projetos[i].codigo == codigo) idxproj = i;
  }

  //incrementa a qtd de participantes e realloca de maneira segura
  projetos[idxproj].num_participantes += 1;
  Pesquisador* paux = realloc(projetos[idxproj].participantes, sizeof(Pesquisador) * projetos[idxproj].num_participantes);
  if (paux == NULL){
    perror("Falha ao adicionar pesquisador em projeto");
    free(projetos[idxproj].participantes);
    exit(1);
  }
  projetos[idxproj].participantes = paux;
  
  //gera um ponteiro para o novo participante para facilitar no futuro
  Pesquisador* novop = &projetos[idxproj].participantes[projetos[idxproj].num_participantes-1];

  printf("Digite o nome do novo pesquisador: ");
  fgets(novop->nome, sizeof(novop->nome), stdin);
  novop->nome[strcspn(novop->nome, "\n")] = '\0'; //tira \n
  printf("Digite a titulacao do novo pesquisador(Doutor/Mestre): ");
  char temptit[TAM_TITULO];
  fgets(temptit, sizeof(temptit), stdin);
  temptit[strcspn(temptit, "\n")] = '\0'; //tira \n

  // converte a titulacao para o Enum
  if (strcmp(temptit, "Mestre") == 0) novop->titulacao = Mestre;
  else novop->titulacao = Doutor;

  printf("Pesquisador adicionado com sucesso!\n");

}


void liberarMemoria(Projeto* projetos, int numProjetos){
  
  //libera todos os vetores de pesquisadores
  for(int i = 0; i < numProjetos; i++){

    free(projetos[i].participantes);
  }
  //libera o vetor de projeto principal
  free(projetos);
}
