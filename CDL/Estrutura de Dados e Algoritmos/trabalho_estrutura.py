import timeit
import random
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
        min_idx = i
        for j in range(i + 1, n):
            if vetor[min_idx] > vetor[j]:
                min_idx = j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
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


def quicksort(vetor):
    if len(vetor) <= 1:
        return vetor
    else:
        pivot = vetor[0]
        less_than_pivot = []
        greater_than_pivot = []

        for x in vetor[1:]:
            if x <= pivot:
                less_than_pivot.append(x)
            else:
                greater_than_pivot.append(x)

        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


def medir_tempo(func, vetor):
    start_time = timeit.default_timer()
    resultado = func(vetor.copy())
    end_time = timeit.default_timer()
    execution_time = (end_time - start_time)
    return execution_time, resultado


tamanho_elementos = int(input("Escolha a quantiade de elementos do vetor que será ordenado: "))
vetor = list(range(tamanho_elementos))
random.shuffle(vetor)

tempo_bubble, resultado_bubble = medir_tempo(bubble_sort, vetor)
time.sleep(3)
print(f"Tempo de execução Bubble Sort: {tempo_bubble:.5f} segundos")
print("Array ordenado (Bubble Sort):", resultado_bubble)

tempo_selection, resultado_selection = medir_tempo(selection_sort, vetor)
time.sleep(3)
print(f"Tempo de execução Selection Sort: {tempo_selection:.5f} segundos")
print("Array ordenado (Selection Sort):", resultado_selection)

tempo_insertion, resultado_insertion = medir_tempo(insertion_sort, vetor)
time.sleep(3)
print(f"Tempo de execução Insertion Sort: {tempo_insertion:.5f} segundos")
print("Array ordenado (Insertion Sort):", resultado_insertion)

tempo_quicksort, resultado_quicksort = medir_tempo(quicksort, vetor)
print(f"Tempo de execução Quick Sort: {tempo_quicksort:.5f} segundos")
print("Array ordenado (Quick Sort):", resultado_quicksort)
