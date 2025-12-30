#include <stdio.h>

int main(){
    int vet[5] = {1, 2, 3, 4, 5};
    int* p = vet;

    printf("Endereço de vet: %p\nValor de p: %p\n", vet, p);
    printf("p[]:\n");
    printf("[0]: %d\t[1]: %d\t[2]: %d\t[3]: %d\t[4]: %d\n", p[0], p[1], p[2], p[3], p[4]);
    printf("*p:\n");
    printf("[0]: %d\t[1]: %d\t[2]: %d\t[3]: %d\t[4]: %d\n", *p, *(p+1), *(p+2), *(p+3), *(p+4));
    printf("vet[]:\n");
    printf("[0]: %d\t[1]: %d\t[2]: %d\t[3]: %d\t[4]: %d\n", vet[0], vet[1], vet[2], vet[3], vet[4]);
    printf("*vet:\n");
    printf("[0]: %d\t[1]: %d\t[2]: %d\t[3]: %d\t[4]: %d\n", *vet, *(vet+1), *(vet+2), *(vet+3), *(vet+4));



    return 0;
}


