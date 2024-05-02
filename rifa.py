# import random

numeros_disponiveis = []
quantidade = int(input("Quantos números estão disponíveis na rifa?\n"))
disponiveis = []
for i in range(quantidade):
    disponiveis = input("Digite um número disponível na rifa")
    numeros_disponiveis.append(disponiveis)
# TODO colocar quantos números você quer sortear
numeros_escolhidos = []
print(f"Há {len(numeros_disponiveis)} números disponíveis na rifa")

# for i in range(6):
#     numeros_escolhidos.append(numeros_disponiveis[random.randint(0, len(numeros_disponiveis) - 1)])
#     print(f"{i+1} número escolhido {numeros_escolhidos[i]}")

# alternativa
# numeros_escolhidos.append(random.sample(numeros_disponiveis, 6))
# print(f"Os 6 números escolhidos foram: {numeros_escolhidos}")