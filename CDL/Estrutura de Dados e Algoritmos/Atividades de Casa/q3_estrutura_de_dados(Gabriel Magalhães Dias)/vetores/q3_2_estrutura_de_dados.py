# Escreva um programa que encontre o maior e o menor valor em um vetor.

vetor = [2, 5, 7, 10, 6, 18]

maior = vetor[0]
menor = vetor[0]

# ou
# maior = max(vetor)
# menor = min(vetor)

for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
print(f"O maior elemento do vetor é {maior}")

for i in range(len(vetor)):
    if vetor[i] < menor:
        menor = vetor[i]
print(f"O menor elemento do vetor é {menor}")

