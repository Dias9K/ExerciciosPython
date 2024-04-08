# Crie um programa que calcule a média dos elementos em uma matriz.

matriz = [[5.0, 1.5, 2.0, 10.0, 7.0],
          [5.5, 3.0, 9.0, 4.0, 6.0],
          [1.5, 0.0, 5.0, 8.0, 7.5]]
total_elementos = 0
quantidade_elementos = 0
for i in range(3):
    for j in range(5):
        quantidade_elementos += 1
        total_elementos += matriz[i][j]
print(total_elementos)
print(f"A média da matriz é {total_elementos/quantidade_elementos}")