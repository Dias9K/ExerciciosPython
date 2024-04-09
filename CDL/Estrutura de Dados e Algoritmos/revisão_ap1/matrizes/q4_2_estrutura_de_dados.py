#  Crie um programa que dado um vetor, devolva 2 outros vetores com o quadrado
# e o cubo dos valores do vetor inicial.

matriz_1 = [[1, 20, 30],
            [20, 30, 1]]
matriz_2 = [[10, 30, 2],
            [20, 30, 1]]
matriz_3 = [[0, 0, 0],
            [0, 0, 0]]

for i in range(2):
    for j in range(3):
        matriz_3[i][j] = matriz_1[i][j] + matriz_2[i][j]

print(matriz_3)
