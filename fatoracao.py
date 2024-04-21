divisores = []
dividendo = 2
for i in range(3):
    numero = input("Digite o números para fazer a fatoração: ")
    divisores.append(numero)

for numero in divisores:
    if numero % dividendo == 0:
        print(f"O número é divisível por {dividendo}")
    else:
        dividendo += 1
