def buscaSequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i  # retornará o índice da lista
    return -1


print(buscaSequencial([3, 6, 8, 10], 10))
