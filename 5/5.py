"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

texto = input("Insira a frase que deseja inverter: ")
# texto = "TargetSistemas"

def inverte_texto(texto):
    texto_invertido: str = ""
    lista = list(texto)
    lista_invertida: list = []

    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
        texto_invertido: str = "".join(lista_invertida)

    return texto_invertido

print(inverte_texto(texto))