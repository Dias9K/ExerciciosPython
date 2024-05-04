import random

numeros_disponiveis = []
quantidade_disponiveis = int(input("Quantos números estão disponíveis na rifa?\n"))
print("Digite quais números estão disponíveis na rifa")

for i in range(quantidade_disponiveis):
    numeros = int(input())
    numeros_disponiveis.append(numeros)

quantidade_pontos = int(input("Quantos pontos você quer colocar na rifa?\n"))
numeros_escolhidos = []

# TODO implementar condicionais pra não quebrar o código
for i in range(len(numeros_disponiveis)):
    numeros_escolhidos.append(random.sample(numeros_disponiveis, quantidade_pontos))
print(f"Os {quantidade_pontos} números escolhidos foram: {numeros_escolhidos[
    random.randint(0, len(numeros_escolhidos)-1)]}")

# for i in range(6): sei lá que foi que eu fiz aqui
#     numeros_escolhidos.append(numeros_disponiveis[random.randint(0, len(numeros_disponiveis) - 1)])
#     print(f"{i+1} número escolhido {numeros_escolhidos[i]}")
