numero = 0

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Exibir extrato [2] Sacar [0] Sair\n"))
    if opcao == 1:
        print("Exibindo extrato...")
        # break PARA a execução na linha que está inserido
    elif opcao == 2:
        for numeral in range(10):
            print(numeral, end=(", "))
        continue 
        print("Sacando...") # PARA a sua execução em todas as linhas seguintes após a sua instanciação
else:
    print("Saindo...")