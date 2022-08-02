'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

n = int(input("Insira um número para gerar a sequência de Fibonnaci: "))
validacao = int(input("Insira um número para verificar se ele está na sequência: "))

t1 = 0
t2 = 1
seq = []

print(f"\nSequência: {t1} -> {t2}", end="")

cont = 3

while cont <= n:
   t3 = t1 + t2
   print(f" -> {t3}", end="")
   t1 = t2
   t2 = t3
   cont += 1
   seq.append(t3)

print(' -> FIM')

if validacao in seq:
    print(f"{validacao} está na sequência.")
else:
    print(f"{validacao} não está na sequência.")
