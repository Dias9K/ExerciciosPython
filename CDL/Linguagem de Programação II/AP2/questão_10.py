# Gabriel Magalhães Dias
# Questão 10 – (0,75 pontos)
# Escreva um programa que compare duas listas. Utilizando operadores de conjuntos imprima:
#  Os valores comuns às duas listas;
#  Os valores que só existem na primeira lista;
#  Os valores que existem apenas na segunda lista;
#  A primeira lista sem os elementos repetidos na segunda lista.
import random

lista_1 = []
lista_2 = []

# adicionando elementos aleatórios nas listas
while len(lista_1) < 5:
    n = random.randint(1, 10)
    lista_1.append(n)

while len(lista_2) < 5:
    u = random.randint(1, 10)
    lista_2.append(u)

# convertendo as listas em conjuntos para que os métodos de set possam ser usados
lista_1 = set(lista_1)
print(f"Elementos do conjunto 1\n{lista_1}")
lista_2 = set(lista_2)
print(f"Elementos do conjunto 2\n{lista_2}")

print(f"Valores comuns das duas listas\n{lista_1.intersection(lista_2)}")
print(f"Valores existentes apenas na primeira lista\n{lista_1.difference(lista_2)}")
print(f"Valores que existem apenas na segunda lista\n{lista_2.difference(lista_1)}")
print(f"Valores não repetidos das duas listas\n{lista_1.symmetric_difference(lista_2)}")
print(f"Valores da primeira lista sem os repetidos da segunda lista\n{lista_2.symmetric_difference(lista_1)}")
