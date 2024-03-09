"""Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos
ou eliminar itens duplicados de um iterável"""

carros = ["palio", "gol", "celta", "palio"]  # declarado em "()", é uma lista
linguagens = {"python", "java", "python"}  # declarado em "{}", é um conjunto, eles não suportam indexação ou fatiamento
# e nem é possível, passar o index para acesso. caso queira acessar os valores, é preciso converter o set em lista
linguagens = list(linguagens)

# retorna os elementos e o seu index
# for carro in enumerate(carros):
#     print(f"{carro}")

for indice, carro in enumerate(carros):
    print(f"{carro}")

# métodos da classe set
# {}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))  # une dois conjuntos

# {}.intersection
conjunto_aa = {1, 2, 3}
conjunto_bb = {2, 3, 4}
print(conjunto_aa.intersection(conjunto_bb))  # retorna os elementos iguais entre dois conjuntos

# {}.difference
conjunto_aaa = {1, 2, 3}
conjunto_bbb = {2, 3, 4}
print(conjunto_aaa.difference(conjunto_bbb))  # retorna o que há de diferente entre os dois conjuntos

# {}.symmetric_difference
conjunto_aaaa = {1, 2, 3}
conjunto_bbbb = {2, 3, 4}
print(conjunto_aaaa.symmetric_difference(
    conjunto_bbbb))  # retorna todos os elementos que não estão na interseção de dois sets

# {}.issubset
conjunto_aaaaa = {1, 2, 3}
conjunto_bbbbb = {4, 1, 2, 5, 6, 3}
print(conjunto_aaaaa.issubset(conjunto_bbbbb))
# verifica se um conjunto é subconjunto de outro, ou seja, se todos os seus elementos estão contidos nesse outro set
print(conjunto_bbbbb.issubset(conjunto_aaaaa))

# {}.issuperset
conjunto_aaaaa = {1, 2, 3}
conjunto_bbbbb = {4, 1, 2, 5, 6, 3}
print(conjunto_aaaaa.issuperset(conjunto_bbbbb))
#  igual o subset, só que ao contrário (?)
print(conjunto_bbbbb.issuperset(conjunto_aaaaa))

#  {}.isdisjoint
conjunto_aaaaaa = {1, 2, 3, 4, 5}
conjunto_bbbbbb = {6, 7, 8, 9}
conjunto_c = {1, 0}
print(conjunto_aaaaaa.isdisjoint(conjunto_bbbbbb))
# verifica se os elementos de um conjunto estão contidos em outro
print(conjunto_aaaaaa.isdisjoint(conjunto_c))

# {}.add
sorteio = {numero for numero in range(1, 6)}  # NÃO PODE USAR O APPEND, ISSO É SÓ PRA LISTAS
sorteio.add(25)  # adiciona um elemento num set já existente
print(sorteio)

# {}.clear limpa o set

# {}.copy copia o set

# {}.discard ou remove/.pop
sorteio.discard(25)
sorteio.remove(5)  # retira um único elemento de um set
sorteio.pop()  # retira o elemento do começo da fila, sem a necessidade de passar um elemento no parâmetro
print(sorteio)

# {}.in verifica se um elemento está presente no set
