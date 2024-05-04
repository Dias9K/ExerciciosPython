import random

numeros_disponiveis = []
quantidade_disponiveis = int(input("Quantos números estão disponíveis na rifa?\n"))
for i in range(quantidade_disponiveis):
    print("Digite quais números estão disponíveis na rifa")
    numeros = int(input())
    numeros_disponiveis.append(numeros)
quantidade_pontos = int(input("Quantos pontos você quer colocar na rifa?"))

numeros_escolhidos = []
for i in range(len(numeros_disponiveis)):
    numeros_escolhidos.append(random)
# TODO gerar números aleatórios com base nos números disponíveis
# for i in range(6):
#     numeros_escolhidos.append(numeros_disponiveis[random.randint(0, len(numeros_disponiveis) - 1)])
#     print(f"{i+1} número escolhido {numeros_escolhidos[i]}")

# alternativa
# numeros_escolhidos.append(random.sample(numeros_disponiveis, 6))
# print(f"Os 6 números escolhidos foram: {numeros_escolhidos}")