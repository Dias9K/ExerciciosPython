frase = "um tigre, dois tigres, tres tigres"
# print(f"Primeira ocorrência: {frase.find("tigre")}")
# print(f"Segunda ocorrência: {frase.find("tigres")}")
# print(f"Segunda ocorrência: {frase.find("tigres", 16)}")

p = 0
while p > -1:
    p = frase.find("tigre", p)  # o método find começa a procurar a partir do valor atual da variável "p"
    if p >= 0:
        print(p)  # printa o início da ocorrência de "tigre"
        p += 1  # soma +1 na variável "p" para que ele encontre a próxima ocorrência no loop
