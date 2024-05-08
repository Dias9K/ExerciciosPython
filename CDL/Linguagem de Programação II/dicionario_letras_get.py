d = {}
palavra = "paralelepipedo"
for letra in palavra:
    d[letra] = d.get(letra, 0) + 1

print(d)