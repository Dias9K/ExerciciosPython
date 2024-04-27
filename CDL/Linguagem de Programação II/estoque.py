estoque = {"Alface": [500, 1.80],
           "Batata": [234, 12.8],
           "Tomate": [432, 5.80],
           "Feijão": [120, 7.87]}

vendas = [["Tomate", 10], ["Batata", 50], ["Alface", 20]]

estoque_atualizado = {}

for item, quantidade in vendas:
    if item in estoque:
        preco_unitario = estoque

# pra comparar
'''# Tabela de produtos e seus preços
tabela = {"Alface": [500, 1.80],
          "Batata": [234, 12.8],
          "Tomate": [432, 5.80],
          "Feijão": [120, 7.87]}

# Vendas de cada produto
vendas = [["Tomate", 10], ["Batata", 50], ["Alface", 20]]

# Criando uma nova tabela para relacionar as informações
relacao = {}
total_geral = 0

for item, quantidade in vendas:
    if item in tabela:
        preco_unitario = tabela[item][1]
        valor_total = quantidade * preco_unitario
        relacao[item] = {"Quantidade Vendida": quantidade, "Preço Unitário": preco_unitario, "Valor Total": valor_total}
        total_geral += valor_total

# Exibindo a tabela relacionada
print("Tabela Relacionada:")
for item, info in relacao.items():
    print(f"{item}: Quantidade Vendida: {info['Quantidade Vendida']}, Preço Unitário: R${info['Preço Unitário']:.2f}, Valor Total: R${info['Valor Total']:.2f}")

print(f"Total Geral: R${total_geral:.2f}")
'''
