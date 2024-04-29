import random

numeros_disponiveis = [2, 3, 4, 6, 8, 10, 11, 15, 18, 20, 22, 25, 28, 29, 30, 31, 34, 35, 36, 37, 38, 40, 41, 42, 43,
                       44, 45, 46, 47, 48, 49, 50, 51, 52,
                       53, 54, 55, 56, 57, 58, 59, 60]

numeros_escolhidos = []
print(f"Há {len(numeros_disponiveis)} números disponíveis na rifa")

for i in range(6):
    numeros_escolhidos.append(numeros_disponiveis[random.randint(0, len(numeros_disponiveis) - 1)])
    print(f"{i+1} número escolhido {numeros_escolhidos[i]}")
