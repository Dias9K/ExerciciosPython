# Gabriel Magalhães Dias
# Questão 17 – (0,75 pontos)
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
# os números.
import operator
from functools import reduce

vetor = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    inteiros = int(numero)
    vetor.append(inteiros)

print(f"Valores contidos no vetor = {vetor}\n"
      f"Soma dos valores contidos no vetor = {sum(vetor)}\n"
      f"Multiplicação dos valores contidos no vetor = {reduce(operator.mul, vetor)}")
# o método reduce, utilizado para reduzir a lista a um único valor de saída, requer uma função e um iterável nos seus
# argumentos, por isso a operator.mul e o próprio vetor de números inteiros

# maneira convencional de iterar os valores do vetor e multiplicá-los
# teste_multiplicador = 1
# for m in vetor:
#     teste_multiplicador = teste_multiplicador*m
# print(f"Multiplicação dos valores contidos no vetor = {teste_multiplicador}")
