def limpar_texto(texto):
    texto_limpo = ''
    for caractere in texto:

        if caractere.isalpha() or caractere.isspace():
            texto_limpo += caractere
    return texto_limpo


def processar_arquivo_alfabeto(nome_arquivo_entrada, nome_arquivo_saida):
    try:
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada, open(nome_arquivo_saida, 'w') as arquivo_saida:
            for linha in arquivo_entrada:
                linha_limpa = limpar_texto(linha)
                arquivo_saida.write(linha_limpa)
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def main():
    nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

    processar_arquivo_alfabeto(nome_arquivo_entrada, nome_arquivo_saida)

    print("Processamento concluído.")


if __name__ == "__main__":
    main()
