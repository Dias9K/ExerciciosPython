print('Realizado por: Gabriel Levi Lima Rodrigues')
# Função criada para ler uma lista de elementos
def contador_caracteres(palavras):
    dicionario = {}
    for caractere in palavras:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1
    return dicionario

# Leitura das palavras
palavras = input('Digite uma frase qualquer: ')

# Gera o dicionario com as contagens dos caracteres
result = contador_caracteres(palavras)

# Exebição do diciionario com as palavras
print(f'O dicionario com as contagens dos carateres: \n {result}')