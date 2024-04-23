import random

vetor = []
for i in range(0, 20):
    vetor.append(random.randint(1, 20))

for i in range(len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[i] > vetor[j]:
            menor = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = menor
print(vetor)