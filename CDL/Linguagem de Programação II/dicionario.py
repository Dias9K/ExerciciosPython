tabela = {"Alface": 1.80,
          "Batata": 12.8,
          "Tomate": 5.80,
          "Feijão": 7.87}

while True:
    escolha = str.upper(input("Quer digitar um elemento? Digite \"Sim\" ou \"Fim\"\n"))
    if escolha == "SIM":
        chave = str(input("Qual a chave do seu elemento?\n"))
        valor = float(input(f"Qual o valor de {chave}?\n"))
        tabela[chave] = valor
        print(tabela)
    elif escolha == "FIM":
        print("Fim da execução...")
        break
