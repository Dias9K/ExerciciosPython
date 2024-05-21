# TODO escolher um algoritmo de ordenação e usar um de busca em um vetor com mil elementos

def binary_search(v, i, f, e):
    if i <= f:
        m = (i + f) // 2
        if e > v[m]:
            return binary_search(v, m + 1, f, e)
        if e < v[m]:
            return binary_search(v, i, m - 1, e)
        else:
            return m
    return -1


vetor = list(range(1, 1000))
print(binary_search(vetor, vetor[0], vetor[len(vetor) - 1], 100))
