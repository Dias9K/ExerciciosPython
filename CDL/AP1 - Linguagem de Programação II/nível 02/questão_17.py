import operator
from functools import reduce
# Questão 17 – (0,75 pontos)
# GABRIEL MAGALHÃES DIAS
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
# os números.

vetor = []
for i in range(5):
    inteiros = int(input("Digite um numero inteiro: "))
# TODO um meio de conversão forçada do float para inteiro
    vetor.append(inteiros)

print(f"Valores contidos no vetor = {vetor}\n"
      f"Soma dos valores contidos no vetor = {sum(vetor)}\n"
      f"Multiplicação dos valores contidos no vetor = {reduce(operator.mul, vetor)}\n")

# TODO terminar isso
print("teste".center(50, "#"))
teste_multiplicador = 0
for m in len(range(vetor)):
    teste_multiplicador * m