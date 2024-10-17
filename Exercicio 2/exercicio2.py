def sequencia(n):
    sequencia = [0, 1]
    while True:
        valor = sequencia[-1] + sequencia[-2]
        if valor > n:
            break
        sequencia.append(valor)
    return sequencia

try:
    numero = int(input("Informe um número: "))
except ValueError:
    print("Por favor, insira um número valido.")
    exit()

verificacao = sequencia(numero)

if numero in verificacao:
    print(f"O número {numero} pertence a sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence a sequência de Fibonacci.")