import random

numeros_disponiveis = []
quantidade_disponiveis = int(input("Quantos números estão disponíveis na rifa?\n"))

print("Digite quais números estão disponíveis na rifa")
for i in range(quantidade_disponiveis):
    numeros = int(input())
    if numeros not in numeros_disponiveis:
        numeros_disponiveis.append(numeros)
    else:
        while True:
            numeros = int(input("O número digitado já existe. Digite um número diferente para que ele possa ser "
                                "adicionado\n"))
            if numeros not in numeros_disponiveis:
                numeros_disponiveis.append(numeros)
                break
        # quase perfeito mais ainda não está
print(f"O números disponíveis na rifa são {numeros_disponiveis}")

numeros_escolhidos = []
while True:
    quantidade_pontos = int(input("Quantos pontos você quer colocar na rifa?\n"))
    if quantidade_pontos > len(numeros_disponiveis):
        print("Quantidade inválida, pois é maior do que a quantidade de números disponíveis")
    else:
        numeros_escolhidos.append(random.sample(numeros_disponiveis, quantidade_pontos))
        break

print(f"Os {quantidade_pontos} números escolhidos foram: {numeros_escolhidos}")

# for i in range(len(numeros_disponiveis)):
#     numeros_escolhidos.append(random.sample(numeros_disponiveis, quantidade_pontos))
# print(numeros_disponiveis)
# print(f"Os {quantidade_pontos} números escolhidos foram: {numeros_escolhidos[
#     random.randint(0, len(numeros_escolhidos)-1)]}")
