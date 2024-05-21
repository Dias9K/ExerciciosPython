# TODO comparar o tempo de execução de dois algoritmos de busca em um vetor com mil elementos
import time


def binary_search(v, i, f, e):
    if i <= f:
        m = (i + f) // 2
        if e > v[m]:
            return binary_search(v, m + 1, f, e)
        elif e < v[m]:
            return binary_search(v, i, m - 1, e)
        else:
            return m
    return -1


vetor = list(range(1, 1000))
chave = 100

antes_binaria = time.time()
posicao = binary_search(vetor, 0, len(vetor) - 1, chave)
depois_binaria = time.time()
tempo_binaria = (depois_binaria - antes_binaria) * 1000  # calculando o tempo de execução da busca binária

if posicao >= 0:
    print("O elemento %d foi encontrado na posição %d." % (chave, posicao))
else:
    print("O elemento %d NÃO foi encontrado." % chave)
print("O tempo de execução do algoritmo de busca binária foi %d", tempo_binaria)
