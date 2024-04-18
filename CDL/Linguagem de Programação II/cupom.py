compra = []
menu = 0
print("MENU".center(20, ":"), "\n[1] Adicionar novo item ao carrinho\n"
                              "[2] Checar quantidade de um determinado item\n"
                              "[3] Checar valor total das unidades de um determinado item\n"
                              "[4] Sair")

item = input("Digite qual item você comprou: ")
quantidade = int(input(f"Digite quantas unidades de {item} você comprou: "))
valor_unitario = float(input(f"Digite o valor da unidade de {item}"))