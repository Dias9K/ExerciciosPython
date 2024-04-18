carrinho = []
menu = 0
while menu != 4:
    print("MENU".center(20, ":"), "\n[1] Adicionar novo item ao carrinho\n"
                                  "[2] Checar quantidade de um determinado item\n"
                                  "[3] Checar valor total das unidades de um determinado item\n"
                                  "[4] Sair")
    try:
        menu = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite uma opção válida!")
    if menu == 1:
        item = input("Digite qual item você comprou: ")
        if len(item) > 0:
            quantidade = int(input(f"Digite quantas unidades de {item} você comprou: "))
            valor_unitario = float(input(f"Digite o valor da unidade de {item}"))
            carrinho.append([item, quantidade, valor_unitario])
        else:
            print("Digite pelo menos um item")
