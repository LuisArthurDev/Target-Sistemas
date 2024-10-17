# Análise de Faturamento Diário

Este projeto apresenta um programa feito em Python que analisa os valores de faturamento diário de uma distribuidora. O programa calcula o menor e o maior valor de faturamento ocorrido em um dia do mês e determina quantos dias tiveram um faturamento superior à média mensal.

## Descrição do Programa

O programa lê um vetor com os valores de faturamento diário de uma distribuidora, ignora os dias sem faturamento e calcula as seguintes métricas:

1. **Menor Faturamento**: O menor valor de faturamento ocorrido em um dia do mês.
2. **Maior Faturamento**: O maior valor de faturamento ocorrido em um dia do mês.
3. **Dias Acima da Média**: O número de dias em que o faturamento diário foi superior à média mensal.

### Lógica do Programa:

1. **Leitura dos Dados**: Os valores de faturamento diário são armazenados em uma lista.
2. **Cálculo do Menor e Maior Faturamento**: Percorre a lista de faturamentos para encontrar os valores mínimo e máximo, ignorando dias sem faturamento.
3. **Cálculo da Média Mensal**: Soma todos os faturamentos válidos e divide pelo número de dias com faturamento para obter a média.
4. **Contagem de Dias Acima da Média**: Conta quantos dias tiveram faturamento superior à média calculada.
5. **Exibição dos Resultados**: Apresenta os resultados para o usuário.

### Saída Esperada:

O programa retornará as seguintes informações:
- O menor faturamento em um dia.
- O maior faturamento em um dia.
- O número de dias em que o faturamento diário foi superior à média mensal.

## Como Executar

### Pré-requisitos:

- Um interpretador Python.

### Execução:

1. Clone este repositório ou copie o código para um arquivo, como `faturamento.py`.
2. Abra um terminal e navegue até o diretório onde o arquivo está localizado.
3. Execute o programa com o comando: python faturamento.py

### Exemplo de Uso:

O programa calculará e exibirá o menor e maior faturamento, além do número de dias em que o faturamento foi superior à média mensal.

## Contribuição

Sinta-se à vontade para fazer fork deste repositório e enviar pull requests com melhorias ou correções.

