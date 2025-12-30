#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TAMANHO_MAXIMO 105

int calcularC(int N, int array[]);

int calcularR(int N, int array[]);

void gerarPalavraBase(char palavraBase[]);

char transformarMaiuscula(char c);

int transformarInt(char c);

int main(){
    // 1. ================
    int N;
    scanf("%d", &N); 
    getchar(); //tirar \n
    int sequencia[N];
    char auxiliar;
    for (int i = 0; i < N; i++){
        scanf("%c", &auxiliar);
        int digito = transformarInt(auxiliar);
        sequencia[i] = digito;
    }
    getchar(); //tirar \n
    // ===================

    //2. =================
    int C = calcularC(N, sequencia);
    // ===================

    // 3. ================
    int R = calcularR(N, sequencia);
    //====================

    // 4. ===============
    char palavraBase[TAMANHO_MAXIMO];
    gerarPalavraBase(palavraBase);
    // ===================

    //5. =================
    printf("%d %d\n", C, R);
    printf("codigo: %s%d%d", palavraBase, C, R);
    // ==================

    return 0;
}


int calcularC(int N, int array[]){
    int somaPares = 0;
    int somaImpares = 0;

    for (int i = 0; i < N; i++){
        if (i % 2 == 0) somaPares += array[i];
        else somaImpares += array[i];
    }
    return (somaPares * 3 + somaImpares) % 10;
}

int calcularR(int N, int array[]){
    int qtdContiguoAtual = 1;
    int qtdContiguoMax = 1;
    
    for (int i = 1; i < N; i++){
        if (array[i] == array[i-1]) qtdContiguoAtual++;
        else qtdContiguoAtual = 1;

        if (qtdContiguoAtual >= qtdContiguoMax) qtdContiguoMax = qtdContiguoAtual;
    }

    return qtdContiguoMax;
}

void gerarPalavraBase(char palavraBase[]){

    scanf("%s", palavraBase);
    char novaPalavra[TAMANHO_MAXIMO];
    int idx = 0;
    for (int i = 0; i < TAMANHO_MAXIMO; i++){
        if (palavraBase[i] == 'a' || palavraBase[i] == 'A') ;
        else if (palavraBase[i] == 'e' || palavraBase[i] == 'E') ;
        else if (palavraBase[i] == 'i' || palavraBase[i] == 'I') ;
        else if (palavraBase[i] == 'o' || palavraBase[i] == 'O') ;
        else if (palavraBase[i] == 'u' || palavraBase[i] == 'U') ;
        else {
            novaPalavra[idx++] = palavraBase[i];
        }
    }
    int tamanhoNova = strlen(novaPalavra);
    if (tamanhoNova > 0){
        for (int i = 0; i < tamanhoNova; i++){
            if (novaPalavra[i] >= 'a')
                novaPalavra[i] = transformarMaiuscula(novaPalavra[i]);
        }
        strcpy(palavraBase, novaPalavra);
    }
    else{
        strcpy(palavraBase, "VOID");
    }
}

char transformarMaiuscula(char c){
    char alfabeto[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (int i = 0; i < 26; i++){
        if (c == alfabeto[i]){
            return alfabeto[i+26];
        }
    }

    return c;
}

int transformarInt(char c){
    char digitos[] = "0123456789";
    for (int i = 0; i < 10; i++){
        if (c == digitos[i]){
            return i;
        }
    }
}
