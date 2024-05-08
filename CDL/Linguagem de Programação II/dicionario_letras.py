d = {}
palavra = "paralelepipedo"
for letra in palavra:
    if letra in d:
        d[letra] = d[letra] +1
    else:
        d[letra] = 1

print(d)