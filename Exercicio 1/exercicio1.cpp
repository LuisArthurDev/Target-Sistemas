#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    int indice = 13, soma = 0, k = 0;
    while (k < indice) {
        k = k + 1;
        soma = soma + k;
    }
    printf("O Valor da Soma e: %d\n", soma);
    printf("Pressione Enter para fechar o programa...");
    cin.get();
    return 0;
}