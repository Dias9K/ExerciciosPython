# import random

numeros_disponiveis = []
quantidade_disponiveis = int(input("Quantos números estão disponíveis na rifa?\n"))
for i in range(quantidade_disponiveis):
    disponiveis = int(input("Digite o número disponível na rifa"))
    numeros_disponiveis.append(disponiveis)
quantidade_pontos = int(input("Quantos pontos você quer colocar na rifa?"))

numeros_escolhidos = []
# TODO gerar números aleatórios

# for i in range(6):
#     numeros_escolhidos.append(numeros_disponiveis[random.randint(0, len(numeros_disponiveis) - 1)])
#     print(f"{i+1} número escolhido {numeros_escolhidos[i]}")

# alternativa
# numeros_escolhidos.append(random.sample(numeros_disponiveis, 6))
# print(f"Os 6 números escolhidos foram: {numeros_escolhidos}")