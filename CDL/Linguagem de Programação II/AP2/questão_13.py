import sys


def mesclar_arquivos(nome_arquivo1, nome_arquivo2, nome_arquivo_saida):
    try:
        with open(nome_arquivo1, 'r') as arquivo1, open(nome_arquivo2, 'r') as arquivo2, open(nome_arquivo_saida,
                                                                                              'w') as arquivo_saida:

            for linha in arquivo1:
                arquivo_saida.write(linha)

            arquivo_saida.write('\n')

            for linha in arquivo2:
                arquivo_saida.write(linha)

        print("Mesclagem concluída. O resultado foi salvo em", nome_arquivo_saida)
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def main():
    if len(sys.argv) != 4:
        print("Uso: python nome_do_programa.py arquivo1 arquivo2 arquivo_saida")
        sys.exit(1)

    nome_arquivo1 = sys.argv[1]
    nome_arquivo2 = sys.argv[2]
    nome_arquivo_saida = sys.argv[3]

    mesclar_arquivos(nome_arquivo1, nome_arquivo2, nome_arquivo_saida)


if __name__ == "__main__":
    main()

# python mesclar_arquivos.py arquivo1.txt arquivo2.txt arquivo_saida.txt
