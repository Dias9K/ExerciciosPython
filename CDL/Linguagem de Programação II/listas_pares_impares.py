import random

lista = []
pares = []
impares = []

for i in range(10):
    lista.append(random.randint(1, 50))

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Elementos contidos na lista: {lista}\n"
      f"Lista de números pares: {pares}\n"
      f"Lista de números ímpares: {impares}")
