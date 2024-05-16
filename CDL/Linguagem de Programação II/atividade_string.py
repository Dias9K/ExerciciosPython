# escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece na string
# ex: TTAAC
# T: 2x
# A: 2x
# C: 1x

string = list(input("Digite uma palavra qualquer: "))  # a palavra de entrada do usuário se torna uma lista
contador_caracteres = {}

print(f"Elementos contidas na lista: {string}")

for elemento in contador_caracteres:
    if elemento in string:
        contador_caracteres[elemento] += 1
    else:
        contador_caracteres[elemento] = 1
for elemento, quantidade in contador_caracteres.items():
    print(elemento, quantidade)
# TODO terminar