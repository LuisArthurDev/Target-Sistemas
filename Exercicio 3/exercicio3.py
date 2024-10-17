import json

def calcular_faturamento(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    valores = [item['valor'] for item in data]

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)

    dias_com_faturamento = [valor for valor in valores if valor > 0]

    if dias_com_faturamento:
        media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    else:
        media_mensal = 0

    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    return menor_faturamento, maior_faturamento, media_mensal, dias_acima_media

filename = 'Exercicio 3/dados.json'

menor, maior, media, dias_acima_media = calcular_faturamento(filename)

print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Média mensal: R$ {media:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
