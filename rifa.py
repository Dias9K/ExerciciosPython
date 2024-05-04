import random

numeros_disponiveis = []
quantidade_disponiveis = int(input("Quantos números estão disponíveis na rifa?\n"))

print("Digite quais números estão disponíveis na rifa")
for i in range(quantidade_disponiveis):
    numeros = int(input())
    if numeros in numeros_disponiveis:
        print("O número digitado já existe")
    else:
        numeros_disponiveis.append(numeros)
        # quase perfeito mais ainda não está
print(f"O números disponíveis na rifa são {numeros_disponiveis}")
quantidade_pontos = int(input("Quantos pontos você quer colocar na rifa?\n"))
numeros_escolhidos = []

for i in range(len(numeros_disponiveis)):
    numeros_escolhidos.append(random.sample(numeros_disponiveis, quantidade_pontos))
print(numeros_disponiveis)
print(f"Os {quantidade_pontos} números escolhidos foram: {numeros_escolhidos[
    random.randint(0, len(numeros_escolhidos)-1)]}")
