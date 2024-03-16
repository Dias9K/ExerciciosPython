# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

# Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# if quantidade_passos > 0:
#     for i in range(1, quantidade_passos + 1):
#         if quantidade_passos == 1:
#             print(f"Explorador: {quantidade_passos} passo")
#         elif quantidade_passos > 1:
#             print(f"Explorador: {i} passos")
#         quantidade_passos += 1
# A SINTAXE DESSA LINGUAGEM É UMA MERDA, FODA-SE A SUA DELIMITAÇÃO DE BLOCO POR IDENTAÇÃO!
# QUEM NASCEU PRA SER PYTHON NUNCA VAI SER JAVA!!
if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
elif quantidade_passos > 0:
    for i in range(1, quantidade_passos):
        if i == 1:
            print(f"Explorador: {i} passo")
        print(f"Explorador: {i+1} passos")
