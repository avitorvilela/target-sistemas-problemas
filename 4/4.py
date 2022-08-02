"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do
valor total mensal da distribuidora.
"""

estados: list = ["SP", "RJ", "MG", "ES", "Outros"]
faturamento: list = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

soma: float = 0.0
percentual: list = []

for i in range(len(faturamento)):
    soma += faturamento[i]

for i in range(len(faturamento)):
    calc = faturamento[i] / (soma/100)
    percentual.append(calc)

print("-" * 3 + "FATURAMENTO MENSAL P/ ESTADO " + "-" * 3 + "\n")

for i in range(len(faturamento)):
    print(f"{estados[i]} - ~{round(percentual[i], 2)} %")

