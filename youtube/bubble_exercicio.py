# 1) Escreva uma função que use o algoritmo Bubble Sort para ordenar essa lista em ordem alfabética. OK
# 2) Teste sua função com a lista de nomes fornecida e verifique se a saída está
# correta. OK


def bubble_sort(v):
    t = len(v)

    while t > 0:
        i = 0
        while i < t - 1:
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                print(v)
            i += 1
        t -= 1


nomes = ["Carlos", "Ana", "Beatriz", "Eduardo", "Daniel", "Fernanda", "Bruna", "Gabriel"]
bubble_sort(nomes)
print(nomes)

