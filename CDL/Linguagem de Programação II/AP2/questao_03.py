print('Realizado por: Gabriel Levi Lima Rodrigues')
# Função para ler uma lista de elementos
def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        elemento = input(f'Digite o elemento {i + 1}: ')
        lista.append(elemento)
    return lista

# Lê o tamanho das duas listas
tamanho1 = int(input('Digite o tamanho da primeira lista: '))
tamanho2 = int(input('Digite o tamanho da segunda lista: '))

# Lê as duas listas
print('Digite os elementos da primeira lista:')
lista1 = ler_lista(tamanho1)

print('Digite os elementos da segunda lista:')
lista2 = ler_lista(tamanho2)

# Combina as duas listas e remove duplicatas usando um conjunto
conjunto_combinado = set(lista1 + lista2)

# Converte o conjunto de volta para uma lista
lista3 = list(conjunto_combinado)

# Exibe a terceira lista sem elementos repetidos
print('A terceira lista sem elementos repetidos é:')
print(lista3)
