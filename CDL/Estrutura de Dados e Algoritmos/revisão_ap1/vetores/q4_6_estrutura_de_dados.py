# Implemente um algoritmo para encontrar o segundo maior valor em um vetor.
import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1, 10))

print(vetor)
maior = 0
segundo_maior = 0

for numero in vetor:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero

print(f"O maior elemento do vetor é: {maior}\nE o segundo maior elemento é: {segundo_maior}")