d = {}
palavra = "paralelepipedo"
for letra in palavra:
    if letra in d:
        # se a letra já estiver no dicionário, é somado +1
        d[letra] = d[letra] + 1
    else:
        # se não houver atribui a letra e atribui 1
        d[letra] = 1

print(d)
