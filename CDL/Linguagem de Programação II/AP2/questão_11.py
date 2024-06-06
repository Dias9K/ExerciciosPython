# Gabriel Magalhães Dias
# Questão 11 – (0,75 pontos)
# Escreva um programa que recebe o nome de um arquivo pela linha de comando e que
# imprima todas as linhas deste arquivo.

import sys

if len(sys.argv) != 2:  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-01.py nome_do_arquivo\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
    arquivo.close()