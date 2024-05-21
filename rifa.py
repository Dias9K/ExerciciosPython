import random
# um gerador de números bastante simplório para que eu não tenha mais problemas de indecisão ao escolher números
# para colocar pontos em uma rifa ou algo do tipo
numeros_disponiveis = []
quantidade_disponiveis = int(input("Quantos números estão disponíveis na rifa?\n"))

print("Digite quais números estão disponíveis na rifa")
# insere os números e verifica se há números repetidos na lista
for i in range(quantidade_disponiveis):
    numeros = int(input())
    # se o número digitado não estiver na lista, ele será adicionado
    if numeros not in numeros_disponiveis:
        numeros_disponiveis.append(numeros)
    else:
        while True:
            # se estiver, entra nesse laço infinito e só sai quando o número digitado não houver na lista
            numeros = int(input("O número digitado já existe. Digite um número diferente para que ele possa ser "
                                "adicionado\n"))
            if numeros not in numeros_disponiveis:
                numeros_disponiveis.append(numeros)
                break

print(f"O números disponíveis na rifa são {numeros_disponiveis}")

# numeros_escolhidos = []
while True:
    # verificação para checar se a quantidade de números desejados é maior do que a quantidade de números disponíveis
    quantidade_pontos = int(input("Quantos pontos você quer colocar na rifa?\n"))
    if quantidade_pontos > len(numeros_disponiveis):
        print("Quantidade inválida, pois é maior do que a quantidade de números disponíveis")
    else:
        # o sample pega da lista 'numeros_disponiveis' a mesma quantidade de 'quantidade_pontos' e os armazena na
        # lista 'numeros_escolhidos'
        numeros_escolhidos = random.sample(numeros_disponiveis, quantidade_pontos)
        break

print(f"Os {quantidade_pontos} números escolhidos foram: {numeros_escolhidos}")

for i in range(len(numeros_disponiveis)):
    numeros_escolhidos.append(random.sample(numeros_disponiveis, quantidade_pontos))
print(numeros_disponiveis)
print(f"Os {quantidade_pontos} números escolhidos foram: {numeros_escolhidos[random.randint(0, len(numeros_escolhidos)-1)]}")
