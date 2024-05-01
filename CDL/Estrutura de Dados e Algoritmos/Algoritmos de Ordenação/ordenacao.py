# ordenar o vetor sem utilizar o método .sort()
vetor = [2, 3, 1, 5, 4]

for i in range(len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[i] > vetor[j]:
            menor = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = menor
print(vetor)