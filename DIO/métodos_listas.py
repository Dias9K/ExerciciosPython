# [].copy()
lista1 = [1, "string", [10, 40, 80]]
lista2 = lista1.copy()  # copia a todos os elementos da lista
print("ID",
      id(lista1), id(lista2)
      )  # o método id serve para retornar uma espécie de "hash" comprovando que são duas instâncias diferentes,
# mas com os mesmos elementos
lista2[0] = 10  # substituição do primeiro elemento da lista2 para 10
print(lista1)
print(lista2)

# [].count()
frutas = ["laranja", "morango", "limão", "laranja", "banana"]
for fruta in frutas:
    #TODO continuar aquiprint(fruta.count(fruta))
# print(frutas.count("laranja"))  # retorna quantas vezes um elemento se repete na lista
# print(frutas.count("morango"))

# [].extend()
linguagens = ["python", "java"]
print(linguagens)
linguagens.extend(
    ["js", "c", "c#", "java"]
)  # acrescenta uma outra lista em uma já existente
print(linguagens)
# [].sort()
linguagens.sort()  # ordena os elementos na ordem alfabética
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)  # ordena os elementos na ordem alfabética descendente
linguagens.sort(
    key=lambda x: len(x)
)  # função anônima que ordena os elementos de acordo com a sua quantidade de caracteres
print(linguagens)
linguagens.sort(
    key=lambda x: len(x), reverse=True
)  # função anônima que ordena os elementos de acordo com a sua quantidade de caracteres e com a ordem alfabética
# descendente
print(linguagens)

# [].index()
print(
    linguagens.index("java")
)  # retorna a primeira ocorrência de um elemento específico

# [].pop()
print(linguagens)
linguagens.pop()  # retira o último item da lista por padrão, conceito de pilha (LIFO)
linguagens.pop(0)  # também pode ser utilizado passando o index
print(linguagens)

# [].remove()
linguagens.remove("java")  # remove um item específico da lista
print(linguagens)

# [].reverse()
linguagens.reverse()  # reverte a ordem dos elementos da lista
print(linguagens)
