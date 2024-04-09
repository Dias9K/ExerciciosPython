# Escreva um programa que intercale os elementos de dois vetores em um terceiro vetor.
import random

vetor_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vetor_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
vetor_3 = []

for i in range(len(vetor_1)):
    vetor_3.append(vetor_1[random.randint(0, 9)])
    vetor_3.append(vetor_2[random.randint(0, 9)])

print(vetor_3)
