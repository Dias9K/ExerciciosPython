estoque = {"Alface": [500, 1.80],
           "Batata": [234, 12.8],
           "Tomate": [432, 5.80],
           "Feijão": [120, 7.87]}

vendas = [["Tomate", 10], ["Batata", 50], ["Alface", 20]]

estoque_atualizado = {}

for item, quantidade in vendas:
    if item in estoque:
        preco_unitario = estoque