import time


def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor


def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(i + 1, n):
            if vetor[i] > vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor


def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    return vetor


vetor = [23, 6, 42, 17, 31, 8, 49, 2, 11, 38, 5, 27, 14, 3, 46, 19, 35, 10, 7, 50]

start_time = time.time()
# resultado_bubble = bubble_sort(vetor.copy())
# só funciona debugando (???)
bubble_sort(vetor)
end_time = time.time()
execution_time_bubble = end_time - start_time
print(f"Tempo de execução bubble: {execution_time_bubble:.7f} segundos")
print("Array crescente ordenado (Bubble Sort):", vetor[:-10])

start_time = time.time()
resultado_selection = selection_sort(vetor.copy())
end_time = time.time()
execution_time_selection = end_time - start_time
print(f"Tempo de execução selection: {execution_time_selection:.7f} segundos")
print("Array crescente ordenado (Selection Sort):", resultado_selection[:-10])

start_time = time.time()
resultado_insertion = insertion_sort(vetor.copy())
end_time = time.time()
execution_time_insertion = end_time - start_time
print(f"Tempo de execução insertion: {execution_time_insertion:.7f} segundos")
print("Array crescente ordenado (Insertion Sort):", resultado_insertion[:-10])
