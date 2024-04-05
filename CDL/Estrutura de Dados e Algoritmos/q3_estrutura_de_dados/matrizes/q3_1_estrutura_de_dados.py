# Implemente um algoritmo para encontrar o maior elemento em uma matriz.

turma = [[5.0, 1.5, 2.0, 10.0, 7.0],
         [5.5, 3.0, 9.0, 4.0, 6.0],
         [1.5, 0.0, 5.0, 8.0, 7.5]]
maior_elemento = 0
for i in range(3):
    for j in range(5):
        if turma[i][j]:
            maior_elemento = turma[i][j]
print(f"O maior elemento é: {maior_elemento}")