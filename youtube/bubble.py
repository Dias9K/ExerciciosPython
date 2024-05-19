import random


def bubble_sort(v):
    fim = len(v)  # determina a quantidade total do vetor e atribui como o fim do vetor;
    # após colocar o maior valor no fim, não é preciso percorrer o vetor novamente até o final e continuar a ordenação;
    # os valores serão ordenados de trás para frente

    while fim > 0:  # enquanto a lista ainda tiver um tamanho, a lista vai sendo ordenada e o "fim" vai diminuindo
        i = 0
        # percorrendo o vetor de 0 até fim
        while i < fim - 1:  # a verificação precisa ser feita até um valor a menos que o fim, para que não seja
            # acessado um índice fora da lista
            if v[i] > v[i + 1]:
                # fazendo swap da posição atual pela próxima
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp
                print(v)
            i += 1
        fim -= 1


vetor = list(range(0, 10))
random.shuffle(vetor)
print(f"Desordenado\n{vetor}")
bubble_sort(vetor)
