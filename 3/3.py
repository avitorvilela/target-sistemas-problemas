"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar,
que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

# Lê o arquivo json e o armazena em uma variável
with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)  # list

dia: list = []
valor: list = []
menor = 50000
maior = 0
media = 0
soma = 0.0
dias_faturamento_igual_zero = 0
dias_faturamento_maior_media = 0
lista_dias_faturamento_maior_media: list = []
# dia_maior = 0
# dia_menor: list = []

# Armazena os dias e os valores em suas respectivas listas
for i in dados:
    dia.append(i['dia'])
    valor.append(i['valor'])

# Armazena o menor valor e o(s) seu(s) respectivos(s) dia(s)
for i in range(len(valor)):
    if valor[i] <= menor:
        menor = valor[i]
        # dia_menor.append(dia[i])

# Armazena o maior valor e o seu respectivo dia
for i in range(len(valor)):
    if valor[i] > maior:
        maior = valor[i]
        # dia_maior = dia[i]

# Faz a média de faturamento mensal e verifica em quais dias ela foi maior do que o faturamento do dia
for i in range(len(valor)):
    if valor[i] == 0.0:
        dias_faturamento_igual_zero += 1

    soma += valor[i]
    media = soma / (len(valor) - dias_faturamento_igual_zero)

    if valor[i] > media:
        # lista_dias_faturamento_maior_media.append(dia[i])
        dias_faturamento_maior_media += 1

if __name__ == '__main__':
    print(f"O menor valor de faturamento ocorrido em um dia do mês: $ {menor}")
    # print(f"Dias: {dia_menor}")
    print(f"O maior valor de faturamento ocorrido em um dia do mês: $ {round(maior, 2)}")
    # print(f"Dia: {dia_maior}")
    print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_faturamento_maior_media}")
    # print(f"Dias: {lista_dias_faturamento_maior_media}")°