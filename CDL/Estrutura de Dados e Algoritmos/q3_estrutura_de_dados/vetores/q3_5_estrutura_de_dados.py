# Crie um programa que conte o número de ocorrências de um determinado elemento em um vetor.
import random

vetor = []
contador = 0

for i in range(10):
    vetor.append(random.randint(1, 5))
print(f"Elementos do vetor: {vetor}")

for i in range(len(vetor)):
    if vetor[i] == 4:
        contador += 1

print(f"O número 4 foi encontrado {contador}x no vetor")