# Cálculo de Soma em Loop

Este projeto é um exemplo simples de um programa em C++ que realiza uma soma sequencial utilizando um loop `while`. O programa acumula a soma de valores incrementados até atingir um índice pré-definido.

## Descrição do Programa

O código começa com três variáveis:
- `INDICE`: O valor máximo que controla o loop. 
- `SOMA`: Armazena a soma acumulada dos valores.
- `K`: Um contador que é incrementado em cada iteração do loop.

O loop continua até que o valor de `K` seja igual ao valor de `INDICE`. A cada iteração, `K` é incrementado em 1 e adicionado à variável `SOMA`.

### Lógica do Programa:

1. **Inicialização**: `SOMA` começa em 0, e `K` começa em 0.
2. **Loop**: Enquanto `K` for menor que `INDICE` (13), ele é incrementado e adicionado à variável `SOMA`.
3. **Resultado**: Após o loop, o valor da soma acumulada é exibido.

### Saída Esperada:

Ao executar o código, o valor final da variável `SOMA` será **91**, pois o programa faz a seguinte sequência de somas:

