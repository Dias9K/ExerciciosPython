continua = True
lista = []
while continua:
    n = int(input("Digite um numero: "))
    lista.append(n)
    op = input("Deseja continuar? (s/n): ")
    if op != "s" and op != "S":
        continua = False
print(lista)
for i in range(len(lista)):
    lista[i] = lista[i] + 1
print(lista)
