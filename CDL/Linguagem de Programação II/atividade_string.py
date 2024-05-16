# escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece na string
# ex: TTAAC
# T: 2x
# A: 2x
# C: 1x

string = list(input("Digite qualquer palavra: "))  # as letras da palavra de entrada do usuário se tornam elementos
# de uma lista
contador_caracteres = {}  # dicionário vazio

print(f"Elementos contidas na lista: {string}")

for elemento in string:  # itera sobre os elementos da lista
    if elemento in contador_caracteres:  # condicionais para adicionar elementos ao contador
        contador_caracteres[elemento] += 1  # caso o elemento já esteja no contador, é somado mais 1
    else:
        contador_caracteres[elemento] = 1  # caso não esteja, o elemento é inicializado em 1
for elemento, quantidade in contador_caracteres.items():
    print(f"O elemento \"{elemento}\" aparece {quantidade}x")
