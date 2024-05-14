# escreva um programa que compare duas listas e imprima:
# a) os valores comuns das duas listas;
# b) os valores que só existem na primeira lista;
# c) os valores que existem apenas na segunda lista;
# d) uma lista com os valores não repetidos das duas listas;
# e) a primeira lista sem os valores repetidos da segunda lista.

lista_1 = [1, 2, 3, 6, 4, 5]
lista_2 = [5, 4, 7, 8, 10]

lista_1 = set(lista_1)
lista_2 = set(lista_2)
print(f"valores comuns das duas listas\n{lista_1.intersection(lista_2)}")
print(f"valores existentes apenas na primeira lista\n{lista_1.difference(lista_2)}")
print(f"valores que existem apenas na segunda lista\n{lista_2.difference(lista_1)}")
print(f"valores não repetidos das duas listas\n{lista_1.symmetric_difference(lista_2)}")
print(f"valores da primeira lista sem os repetidos da segunda lista\n{lista_2.symmetric_difference(lista_1)}")
