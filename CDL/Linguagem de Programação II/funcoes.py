frase = "um tigre, dois tigres, tres tigres"
# print(f"Primeira ocorrência: {frase.find("tigre")}")
# print(f"Segunda ocorrência: {frase.find("tigres")}")
# print(f"Segunda ocorrência: {frase.find("tigres", 16)}")

p = 0
while p > -1:
    p = frase.find("tigre", p)
    if p >= 0:
        print(p)
        p += 1
