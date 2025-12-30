#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 1000
#define SLICE_SIZE 50

typedef enum {
  NAO_PERIODICO,
  PERIODICO,
} Periodo;

typedef enum {
  PERDEU,
  VENCEU,
} Resultado;

typedef struct {
  int amplitude;
  int frequencia;
  float energia;
  Periodo flag;
  int pontos;
} Sinal;

Sinal lerSinal(char* inp);

Sinal* lerInimigos(int* n);

Resultado batalhar(Sinal* cremosa, Sinal* desafiante);

void selectionSortInimigos(Sinal* inimigos, int qtd_inimigos, Resultado* registro);
  
void printarResultados(Sinal* cremosa, Sinal* inimigos, int qtd_inimigos, Resultado* registro, int fl, int winner);

int main(){
  char temp[MAX_SIZE];
  fgets(temp, sizeof(temp), stdin);
  Sinal cremosa = lerSinal(temp);
  cremosa.pontos = 0;

  int qtd_batalhas = 0;
  Sinal* inimigos = lerInimigos(&qtd_batalhas);
  
  Resultado registro[qtd_batalhas];
  int flawless = 1;
  int winner = 0;
  for (int i = 0; i < qtd_batalhas; i++){
    registro[i] = batalhar(&cremosa, &inimigos[i]);
    if (registro[i] == PERDEU) flawless = 0;
    else winner = 1;
  }
  selectionSortInimigos(inimigos, qtd_batalhas, registro);

  printarResultados(&cremosa, inimigos, qtd_batalhas, registro, flawless, winner);
    
  free(inimigos);

  return 0;
}

Sinal lerSinal(char* inp){

  // amp freq energ flag(str);
  Sinal temp = {0, 0, 0.0, NAO_PERIODICO};
  char strflag[SLICE_SIZE];
  strcpy(strflag, "FALSE");

  // desisti do parser manual e fui pro sscanf......
  int qtd_lidos = sscanf(inp, "%d %d %f %s", &temp.amplitude, &temp.frequencia, &temp.energia, strflag);
  
  if (qtd_lidos == 3){
    fgets(strflag, sizeof(strflag), stdin);
    strflag[strcspn(strflag, "\n")] = '\0';
  }
  // por algum motivo strcmp retorna 0 se for true
  if (strcmp(strflag, "TRUE") == 0) temp.flag = PERIODICO;
  else if (strcmp(strflag, "FALSE") == 0 ) temp.flag = NAO_PERIODICO; 

  return temp;
}

Sinal* lerInimigos(int* n){
  
  Sinal* inimigos = NULL;
  int qtd_inimigos = 0;
  int idx = 0;

  char buff[MAX_SIZE];
  while(fgets(buff, sizeof(buff), stdin) != NULL){
    qtd_inimigos++;
    idx = qtd_inimigos - 1;
    Sinal* auxIni = realloc(inimigos, sizeof(Sinal) * qtd_inimigos);
    if (auxIni == NULL){
      if (inimigos != NULL) free(inimigos);
      exit(1);
    }
    inimigos = auxIni;

    inimigos[idx] = lerSinal(buff);
  }
  *n = qtd_inimigos;
  return inimigos;
}

Resultado batalhar(Sinal* cremosa, Sinal* desafiante){
  int cremosa_pts = 0;
  desafiante->pontos = 0;
  
  // amplitude
  if (cremosa->amplitude > desafiante->amplitude) cremosa_pts++;
  else if (cremosa->amplitude < desafiante->amplitude) desafiante->pontos++;
  
  // freq
  if (cremosa->frequencia == desafiante->frequencia){
    cremosa_pts++; desafiante->pontos++;
  }
  else if (desafiante->frequencia != 0 && (cremosa->frequencia % desafiante->frequencia) == 0) cremosa_pts++;
  else if (cremosa->frequencia != 0 && (desafiante->frequencia % cremosa->frequencia) == 0) desafiante->pontos++;
 
  // energia
  if (cremosa->energia > desafiante->energia) cremosa_pts++;
  else if (cremosa->energia < desafiante->energia) desafiante->pontos++;
  
  // periodico
  if (cremosa->flag == PERIODICO && desafiante->flag == NAO_PERIODICO) cremosa_pts++;
  else if (cremosa->flag == NAO_PERIODICO && desafiante->flag == PERIODICO) desafiante->pontos++;
  
  if (cremosa_pts > cremosa->pontos) cremosa->pontos = cremosa_pts;

  if (cremosa_pts <= desafiante->pontos) return PERDEU;  
  else return VENCEU;
}

void selectionSortInimigos(Sinal* inimigos, int qtd_inimigos, Resultado* registro){

  
  for (int i = 0; i < qtd_inimigos; i++){
      int big = i;
    for (int j = i+1; j < qtd_inimigos; j++){
      if (inimigos[j].pontos > inimigos[big].pontos) big = j;
    }
    Sinal temps = inimigos[i];
    inimigos[i] = inimigos[big];
    inimigos[big] = temps;

    Resultado tempr = registro[i];
    registro[i] = registro[big];
    registro[big] = tempr;
  }

}


void printarResultados(Sinal* cremosa, Sinal* inimigos, int qtd_inimigos, Resultado* registro, int fl, int winner){
  
  printf("%d %d %.2f %d", cremosa->amplitude, cremosa->frequencia, cremosa->energia, cremosa->pontos); 
  
  if (winner){
    printf(" WINNER ( ");
    for (int i = 0; i < qtd_inimigos; i++){
      if (registro[i] == VENCEU) printf("%d ", i+1);
    }
    printf(")\n");
  }

  else printf("\n");
  
  printf("---\n");

  for (int i = 0; i < qtd_inimigos; i++){
    printf("%d %d %.2f %d", inimigos[i].amplitude, inimigos[i].frequencia, inimigos[i].energia, inimigos[i].pontos);

    if (registro[i] == PERDEU) printf(" WINNER\n");
    else printf("\n");
  }

  if (fl) printf("FLAWLESS VICTORY!\n");
}

