#include <stdio.h>

int main() {
  char input[101];
  fgets(input, 100, stdin); // podia ser scanf("%[^\n]", input), ou
                            // scanf("%100s", input)  também

  // pega quantidade de palavras na string e o índice onde cada uma começa
  int qtd_palavras = 0;
  int palavras_idx[50];
  palavras_idx[qtd_palavras++] = 0;
  for (int i = 0; input[i] != '\0'; i++) {
    if (input[i] == ' ' || input[i] == '\n') {
      palavras_idx[qtd_palavras++] = i + 1;
    }
  }

  for (int i = 0; i < qtd_palavras - 1; i++) {
    for (int j = i + 1; j < qtd_palavras - 1; j++) {
      int idx_primeira = palavras_idx[i];
      int idx_segundas = palavras_idx[j];
      int tam_primeira = palavras_idx[i + 1] - palavras_idx[i] - 1;
      int tam_segunda = palavras_idx[j + 1] - palavras_idx[j] - 1;

      if (tam_primeira == tam_segunda) {
        int qtd_diferentes = 0;
        for (int k = 0; k < tam_primeira; k++) {
          if (input[idx_primeira + k] != input[idx_segundas + k]) {
            qtd_diferentes++;
          }
        }

        if (qtd_diferentes == 1) {:wq

          // adicionar nas respostas ambas
        }
      }
      int sub = tam_primeira - tam_segunda;
      if (sub == 1 || sub == -1) {
        int qtd_diferentes = 0;
        int tam_menor = 0;
        int tam_maior = 0;
        if (sub == 1) {
          tam_menor = tam_segunda;
          tam_maior = tam_primeira;
        } else {
          tam_menor = tam_primeira;
          tam_maior = tam_segunda;
        }
      }

      for (int i = 0, j = 0; i < tam_menor && j < tam_maior;) {
        input[idx]
      }
    }
  }

  return 0;
}
