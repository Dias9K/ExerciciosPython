def buscaSequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i  # retornará o índice da lista
    return "A chave digitada não foi encontrada na lista!"


print(buscaSequencial([3, 6, 9, 10], 11))
