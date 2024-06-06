# Gabriel Magalhães Dias
# Questão 11 – (0,75 pontos)
# Escreva um programa que recebe o nome de um arquivo pela linha de comando e que
# imprima todas as linhas deste arquivo.

import sys


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())  # Remove espaços em branco no início e fim da linha
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_programa.py nome_do_arquivo")
    else:
        nome_arquivo = sys.argv[1]
        ler_arquivo(nome_arquivo)
