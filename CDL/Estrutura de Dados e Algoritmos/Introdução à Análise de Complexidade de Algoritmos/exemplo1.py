import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1, 100))
    print(vetor)

maior = vetor[0]
for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        print(maior)