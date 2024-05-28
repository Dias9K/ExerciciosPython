# import time

# def bubble_sort(vetor):
#     n = len(vetor)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if vetor[j] > vetor[j + 1]:
#                 vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
#     return vetor


# def selection_sort(vetor):
#     n = len(vetor)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if vetor[i] > vetor[j]:
#                 vetor[i], vetor[j] = vetor[j], vetor[i]
#     return vetor


# def insertion_sort(vetor):
#     for i in range(1, len(vetor)):
#         chave = vetor[i]
#         j = i - 1
#         while j >= 0 and chave < vetor[j]:
#             vetor[j + 1] = vetor[j]
#             j -= 1
#         vetor[j + 1] = chave
#     return vetor

# def quicksort(vetor):
#     if len(vetor) <= 1: # enquanto o tamanho do vetor for maior ou igual a 1
#         return vetor
#     else:
#         # Escolhendo o pivô (aqui estamos escolhendo o primeiro elemento)
#         pivot = vetor[0]
#         # Sublistas para elementos menores e maiores que o pivô
#         less_than_pivot = [x for x in vetor[1:] if x <= pivot]
#         greater_than_pivot = [x for x in vetor[1:] if x > pivot]

#         # Recursão e combinação dos resultados
#         return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# vetor = [23, 6, 42, 17, 31, 8, 49, 2, 11, 38, 5, 27, 14, 3, 46, 19, 35, 10, 7, 50]

# start_time = time.time()
# print(f'start: {start_time}')
# # resultado_bubble = bubble_sort(vetor.copy())
# # só funciona debugando (???)
# bubble_sort(vetor)
# end_time = time.time()
# print(f'end: {end_time}')
# execution_time_bubble = end_time - start_time
# print(f"Tempo de execução bubble: {execution_time_bubble:.2f} segundos")
# print("Array crescente ordenado (Bubble Sort):", vetor)

# start_time = time.time()
# print(f'start: {start_time}')
# selection_sort(vetor)
# #resultado_selection = selection_sort(vetor.copy())
# end_time = time.time()
# print(f'end: {end_time}')
# execution_time_selection = end_time - start_time
# print(f"Tempo de execução selection: {execution_time_selection:.2f} segundos")
# #print("Array crescente ordenado (Selection Sort):", resultado_selection)

# start_time = time.time()
# print(f'start: {start_time}')
# resultado_insertion = insertion_sort(vetor.copy())
# end_time = time.time()
# print(f'end: {end_time}')
# execution_time_insertion = end_time - start_time
# print(f"Tempo de execução insertion: {execution_time_insertion:.2f} segundos")
# print("Array crescente ordenado (Insertion Sort):", resultado_insertion)

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


def quicksort(vetor):
    if len(vetor) <= 1:
        return vetor
    else:
        pivot = vetor[0]
        less_than_pivot = [x for x in vetor[1:] if x <= pivot]
        greater_than_pivot = [x for x in vetor[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# Vetor de exemplo
vetor = [23, 6, 42, 17, 31, 8, 49, 2, 11, 38, 5, 27, 14, 3, 46, 19, 35, 10, 7, 50]


# Função para medir o tempo de execução
end_time = time.time()


# Medindo o tempo de execução de cada algoritmo
start_time = time.time()
bubble_sort(vetor)
print(f"Tempo de execução Bubble Sort: {bubble_time:.4f} segundos")
bubble_time = (end_time - start_time) * 1000

time.sleep(1)

print(f"Tempo de execução Selection Sort: {selection_time:.4f} segundos")
selection_time = (end_time - start_time) * 1000


time.sleep(1)

print(f"Tempo de execução Insertion Sort: {insertion_time:.4f} segundos")
insertion_time = (end_time - start_time) * 1000


time.sleep(1)

print(f"Tempo de execução Quick Sort: {quicksort_time:.4f} segundos")
quicksort_time = (end_time - start_time) * 1000
