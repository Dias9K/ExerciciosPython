# Implemente um algoritmo para encontrar a soma de todos os elementos pares em um vetor.
import random

vetor = []
pares = []
for i in range(5):
    vetor.append(random.randint(1, 10))
print(f"Elementos inseridos no vetor {vetor}")

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        pares.append(vetor[i])
print(f"Elementos pares inseridos no vetor {pares}\n"
      f"Soma dos elementos pares {sum(pares)}")
