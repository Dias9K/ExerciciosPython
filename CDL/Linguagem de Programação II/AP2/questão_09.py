# Gabriel Magalhães Dias
# Questão 09 – (0,75 pontos)
# Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu
# valor seja o número deste caractere encontrado em uma frase lida.
# Exemplo: O rato -> {"O":1, "r":’, "a":1, "t":1, "o": 1}

d = {}
frase = input("Digite uma frase: ")
for letra in frase:
    if letra in d:
        # se a letra já estiver no dicionário, é somado +1
        d[letra] = d[letra] + 1
    else:
        # se não houver atribui a letra e atribui 1
        d[letra] = 1

print(d)
