# Escreva um programa que encontre o maior e o menor valor em um vetor.

import random

vetor = []

for i in range(10):
    vetor.append(random.randint(1, 10))
print(vetor)

maior = vetor[0]
menor = vetor[0]
for numero in vetor:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Maior número : {maior}")
print(f"Menor número : {menor}")
