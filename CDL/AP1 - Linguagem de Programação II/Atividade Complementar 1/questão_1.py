# Questão 01 - ESCREVA UM PROGRAMA QUE EXIBE UMA LISTA DE OPÇÕES (MENU): ADIÇÃO,SUBTRAÇÃO, MULTIPLICAÇÃO,
# DIVISÃO E SAIR. ESTE PROGRAMA DEVE, A PARTIR DA OPERAÇÃO SELECIONADA, SOLICITAR DOIS NÚMEROS, REALIZAR A OPERAÇÃO
# E MOSTRAR O RESULTADO. ENQUANTO O USUÁRIO NÃO DIGITAR A OPÇÃO SAIR O PROGRAMA CONTINUA MOSTRANDO O MENU AO FINAL DE
# CADA OPERAÇÃO.

print("MENU".center(33, "="), "\nEscolha uma opção válida")
menu = 1
while menu != 0:

    menu = int(input("[1] ADIÇÃO\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n[0] SAIR\n"))
    if menu == 1:
        numero_1 = int(input("Digite dois números para somar\n"))
        numero_2 = int(input())
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
        continue
    elif menu == 2:
        numero_1 = int(input("Digite dois números para subtrair\n"))
        numero_2 = int(input())
        print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
        continue
    elif menu == 3:
        numero_1 = float(input("Digite dois números para multiplicar\n"))
        numero_2 = float(input())
        print(f"{numero_1} x {numero_2} = {numero_1 * numero_2}")
        continue
    elif menu == 4:
        numero_1 = float(input("Digite dois números para dividir\n"))
        numero_2 = float(input())
        print(f"{numero_1} : {numero_2} = {numero_1 / numero_2:.1f}")
        continue
    elif menu == 0:
        print("Saindo...")
        break
