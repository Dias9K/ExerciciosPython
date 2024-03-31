# Gabriel Magalhães Dias
# Questão 17 – (0,75 pontos)
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
# os números.
import operator
from functools import reduce


vetor = []
for i in range(5):
    numero = float(input("Digite um numero: "))  # pode ou não receber um float
    inteiros = int(numero)  # caso o vetor contenha algum float, ele é convertido para int
    vetor.append(inteiros)

print(f"Valores contidos no vetor = {vetor}\n"
      f"Soma dos valores contidos no vetor = {sum(vetor)}\n"
      f"Multiplicação dos valores contidos no vetor = {reduce(operator.mul, vetor)}\n")

# teste_multiplicador = 1
# for m in vetor:
#     teste_multiplicador = teste_multiplicador*m
# print(f"Multiplicação dos valores contidos no vetor = {teste_multiplicador}")
