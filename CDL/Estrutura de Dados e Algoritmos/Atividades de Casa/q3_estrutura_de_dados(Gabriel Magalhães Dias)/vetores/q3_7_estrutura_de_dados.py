# Escreva um programa que remova elementos duplicados de um vetor.

vetor = [1, 1, 3, 3, 4, 2, 2, 3, 10, 10,]
vetor_sem_duplicado = []
for elemento in vetor:
    if elemento not in vetor_sem_duplicado:
        vetor_sem_duplicado.append(elemento)
print(vetor_sem_duplicado)