"""
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:
- "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns
casos, é necessário converter/tratar os dados de entrada;
- "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a
impressão dos dados de saída.
"""

n = int(input())
for i in range(n):
    x, y = input().split()
    teste = 0
    cont = 0
    if len(x) < len(y):
        print("nao encaixa")

    else:
        for j in range(len(y)):
            teste -= 1
            if x[teste] == y[teste]:
                cont += 1

        if cont == len(y):
            print("encaixa")
        else:
            print("nao encaixa")
'''
TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
"encaixa" ou "não encaixa" para cada uma das relações N vezes.
'''