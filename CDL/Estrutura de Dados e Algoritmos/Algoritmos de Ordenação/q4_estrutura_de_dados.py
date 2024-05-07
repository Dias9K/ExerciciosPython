# CÓDIGO CORRIGIDO 100%
import random

vetor_desordenado = []
for i in range(0, 20):
    vetor_desordenado.append(random.randint(1, 20))

print("Desordenado")
print(vetor_desordenado)

# Ordenação crescente
for i in range(len(vetor_desordenado)):
    for j in range(i + 1, len(vetor_desordenado)):
        if vetor_desordenado[i] > vetor_desordenado[j]:
            # "Atribuição dupla" pois a posição de dois valores do vetor desordenado estão sendo trocadas ao mesmo tempo
            vetor_desordenado[i], vetor_desordenado[j] = vetor_desordenado[j], vetor_desordenado[i]

# Primeiros 10 elementos em ordem crescente com fatiamento de listas
vetor_1 = vetor_desordenado[:10]
print("Ordem crescente")
print(vetor_1)

# Ordenação decrescente
for i in range(len(vetor_desordenado)):
    for j in range(i + 1, len(vetor_desordenado)):
        if vetor_desordenado[i] < vetor_desordenado[j]:
            vetor_desordenado[i], vetor_desordenado[j] = vetor_desordenado[j], vetor_desordenado[i]

# Primeiros 10 elementos em ordem decrescente
vetor_2 = vetor_desordenado[:10]
# O fatiamento não é capaz de remover os elementos restantes do vetor que foi fatiado
print("Ordem decrescente")
print(vetor_2)
