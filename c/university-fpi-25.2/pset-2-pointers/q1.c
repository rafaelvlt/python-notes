//Questão 1 LE2
#include <stdio.h>

int main(){
    char c = 'a';
    char* pc = &c;

    printf("Endereço de c: %p\nValor de c: %c\n", &c, c);

    printf("Valor de pc: %p\nValor do endereço apontado por pc: %c\n", pc, *pc);

    printf("Endereço de pc: %p\n");

    /*
        Os endereços são iguais devido aos operadores & e * serem opostos.
        Quando é acessado o valor pelo qual o ponteiro pc aponta, e é pego o endereço
        desse valor, será o mesmo endereço que está armazenado em pc.
          Assim como quando é pego o endereço de pc e dereferenciado esse endereço
        é retornado o valor guardado por pc desde o início.
    */
    printf("Endereço do valor guardado no endereço apontado por pc: %p\n", &*pc);
    printf("Valor guardado no endereço de pc: %p\n", *&pc);


    return 0;
}

