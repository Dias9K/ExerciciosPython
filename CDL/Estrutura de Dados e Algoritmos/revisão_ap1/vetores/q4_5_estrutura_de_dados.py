# Implemente um algoritmo para encontrar a soma de todos os elementos pares em
# um vetor.

import random

vetor = []
soma_pares = 0
pares = []

for i in range(10):
    vetor.append(random.randint(0, 10))
print(f"Números inseridos no vetor: {vetor}")

# for par in vetor:
#     if par % 2 == 0:
#         soma_pares += par
#         print(par)
# print(f"A soma dos pares é: {soma_pares}")

for par in vetor:
    if par % 2 == 0:
        pares.append(par)
print(f"Números pares inseridos no vetor: {pares}")
print(f"A soma dos pares é: {sum(pares)}")