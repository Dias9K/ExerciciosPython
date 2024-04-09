# Implemente um algoritmo para somar duas matrizes.

matriz_1 = [[5.0, 1.5, 2.0, 10.0, 7.0],
            [5.5, 3.0, 9.0, 4.0, 6.0],
            [1.5, 0.0, 5.0, 8.0, 7.5]]

matriz_2 = [[5.0, 1.5, 2.0, 10.0, 7.0],
            [5.5, 3.0, 9.0, 4.0, 6.0],
            [1.5, 0.0, 5.0, 8.0, 7.5]]

for i in range(3):
    for j in range(5):
        print(f"{matriz_1[i][j]} + {matriz_2[i][j]} = {matriz_1[i][j] + matriz_2[i][j]}")
