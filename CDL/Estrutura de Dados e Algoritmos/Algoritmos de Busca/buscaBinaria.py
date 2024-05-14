def buscaBinaria(vetor_ordenado, chave):
    for i in range(len(vetor_ordenado)):
        inicio = 0
        fim = vetor_ordenado[-1]

        while len(vetor_ordenado) >= 1:
            meio = (inicio + fim) / 2
            if vetor_ordenado[meio] == chave:
                return meio
            elif vetor_ordenado[meio] > chave:
                fim = meio - 1
                return meio
            elif vetor_ordenado[meio] < chave:
                inicio = meio + 1
                return meio


print(buscaBinaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
