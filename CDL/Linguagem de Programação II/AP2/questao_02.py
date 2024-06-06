print('Realizado por: Gabriel Levi Lima Rodrigues')
# Função para ler uma lsita de elementos;
def Leitura_da_Lista(tamanho):
    lista = []
    for i in range(tamanho):
        elemento = input(f'Digite o elemento {i + 1}°: ')
        lista.append(elemento)
    return lista

# Realiza a leitura das duas lista.
tamanha_1 = int(input('Informe o tamnho da primeira lista: '))
tamanha_2 = int(input('Informe o tamanho da segunda lista: '))

# Leitura das duas Lista
print('Digite os elementos da primeira lista: ')
lista_1 = Leitura_da_Lista(tamanha_1)

print('Digite os elementos da segunda Lista: ')
lista_2 = Leitura_da_Lista(tamanha_2)

# geração da terceira lista combinando as duas primeiras
lista_3 = lista_1 + lista_2

print(f'A terceira lista: {lista_3}')