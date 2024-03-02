opcao = -1
while opcao != 0:
    opcao = int(input("[1] Exibir extrato [2] Sacar [0] Sair\n"))
    if opcao == 1:
        print("Exibindo extrato...")
    elif opcao == 2:
        print("Sacando...")
else:
    print("Saindo...")
# TODO break