# Implemente um algoritmo para verificar se um vetor está ordenado de forma crescente.

vetor = [6, 2, 3, 10, 26, 23, 20, 10]
vetor_sem_copia = []
for elemento in vetor:
    if elemento not in vetor_sem_copia:
        vetor_sem_copia.append(elemento)
vetor_sem_copia.sort()
print(vetor_sem_copia)