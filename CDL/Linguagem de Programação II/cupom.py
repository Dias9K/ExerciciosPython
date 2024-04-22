carrinho = []
menu = 0
item = ""
quantidade = 0
valor_unitario = 0
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
            valor_unitario = float(input(f"Digite o valor da unidade de {item}: "))
            carrinho.append([item, quantidade, valor_unitario])
        else:
            print("ERRO! É obrigatório digitar um item!")
    elif menu == 2:
        item_checado = input("Digite o item a ser checado: ")
        if len(item) == 0 or item_checado != item:
            print("O carrinho de compras está vazio ou o item digitado não foi encontrado")
        elif item_checado == item:
            print(f"{item} == {quantidade}")
    elif menu == 3:
        item_checado = input("Digite o item para ver a o seu valor total: ")
        if item_checado == item:
            print(f"{item} == {valor_unitario * quantidade}")
        elif item_checado != item:
            print(f"Item não encontrado no carrinho")
    else:
        print("Obrigado e volte sempre!".center(40, "-"))
        break
