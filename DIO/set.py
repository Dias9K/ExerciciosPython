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