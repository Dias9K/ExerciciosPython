# Crie um programa que conte o número de ocorrências de um determinado
# elemento em um vetor.

import random

vetor = []

for i in range(1, 6):
    vetor.append(random.randint(1, 6))

print(vetor)
numero_buscado = int(input("Digite o número a ser contado: "))
contador = 0
for i in range(len(vetor)):
    if vetor[i] == numero_buscado:
        contador += 1
print(contador)
