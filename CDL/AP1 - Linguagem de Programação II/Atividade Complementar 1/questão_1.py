# Questão 01 - ESCREVA UM PROGRAMA QUE EXIBE UMA LISTA DE OPÇÕES (MENU): ADIÇÃO,SUBTRAÇÃO, MULTIPLICAÇÃO,
# DIVISÃO E SAIR. ESTE PROGRAMA DEVE, A PARTIR DA OPERAÇÃO SELECIONADA, SOLICITAR DOIS NÚMEROS, REALIZAR A OPERAÇÃO
# E MOSTRAR O RESULTADO. ENQUANTO O USUÁRIO NÃO DIGITAR A OPÇÃO SAIR O PROGRAMA CONTINUA MOSTRANDO O MENU AO FINAL DE
# CADA OPERAÇÃO.

print("MENU".center(33, "="), "\n")


def selecao_menu():
    menu = input("[1] ADIÇÃO\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n[0] SAIR")
    numero_1 = int(input("Digite dois números para somar"))
    numero_2 = int(input())
    if menu == 1:
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
