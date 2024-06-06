import sys


def paginar_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    try:
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada, open(nome_arquivo_saida, 'w') as arquivo_saida:
            linha_atual = 0
            pagina_atual = 1
            arquivo_original = nome_arquivo_entrada

            for linha in arquivo_entrada:
                linha = linha.rstrip()

                if len(linha) > 76:
                    print(
                        f"A linha {linha} no arquivo {nome_arquivo_entrada} excede o limite de 76 caracteres e será ignorada.")
                    continue

                arquivo_saida.write(linha + '\n')
                linha_atual += 1

                if linha_atual == 60:
                    arquivo_saida.write(f"Página {pagina_atual} | Arquivo: {arquivo_original}\n\n")
                    linha_atual = 0
                    pagina_atual += 1

            if linha_atual > 0:
                arquivo_saida.write(f"Página {pagina_atual} | Arquivo: {arquivo_original}\n")

        print("Paginação concluída. O resultado foi salvo em", nome_arquivo_saida)
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def main():
    if len(sys.argv) != 3:
        print("Uso: python nome_do_programa.py arquivo_entrada arquivo_saida")
        sys.exit(1)

    nome_arquivo_entrada = sys.argv[1]
    nome_arquivo_saida = sys.argv[2]

    paginar_arquivo(nome_arquivo_entrada, nome_arquivo_saida)


if __name__ == "__main__":
    main()

# python paginar_arquivo.py texto.txt paginação.txt
