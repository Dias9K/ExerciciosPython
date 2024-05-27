# a ordenação feita pelo selection é basicamente selecionando e colocando os menores elementos no início do vetor
import random


def selection_sort(v):
    i = 0
    # indica inicialmente o menor elemento
    while i < len(v) - 1:  # o i vai percorrer até a penúltima posição do vetor, por isso é menor que o tamanho -1
        menor = i  # a cada loop é atribuído o i como o índice de menor valor
        j = i + 1  # o j sempre estará a uma posição na frente do i

        # verificando se o i (menor) realmente é o menor elemento
        while j < len(v):
            if v[j] < v[menor]:  # caso o j seja menor do que o menor atual, menor receberá o valor de j
                menor = j
            j += 1
        if menor != i:  # caso a variável menor seja diferente que i, a troca é feita
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        i += 1


vetor = list(range(0, 10))
random.shuffle(vetor)
selection_sort(vetor)
print(vetor)
