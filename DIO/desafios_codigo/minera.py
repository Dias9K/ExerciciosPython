capacidade_atual, aumento_percentual = map(int, input().split())
# em um único input são recebido dois valores e que serão armazenados nas suas respectivas variáveis, desde que esses
# estejam separados por um ESPAÇO ex: "100 20". contudo ainda não entendi para que serve esse método map()

# Calcule a nova capacidade do disco de Mithril
novo_valor = capacidade_atual + (capacidade_atual*aumento_percentual/100)

# Imprima a nova capacidade
print(int(novo_valor))