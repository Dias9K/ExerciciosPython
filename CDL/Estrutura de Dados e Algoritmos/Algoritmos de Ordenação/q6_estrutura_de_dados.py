import random
import time

inicio_time = time.time()

# atribuição dos 1000 elementos no vetor usado pelo bubble sort
vetor_bubble = []
for i in range(0, 1000):
    vetor_bubble.append(random.randint(1, 1000))

# atribuição dos 1000 elementos no vetor usado pelo selection sort
vetor_selection = []
for i in range(0, 1000):
    vetor_selection.append(random.randint(1, 1000))

# atribuição dos 1000 elementos no vetor usado pelo insertion sort
vetor_insertion = []
for i in range(0, 1000):
    vetor_insertion.append(random.randint(1, 1000))


def bubble_sort(arr):
    # função com bubble
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    # função com selection
    for i in range(len(arr)):
        idx_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min]:
                arr[j], arr[idx_min] = arr[idx_min], arr[j]
    return arr


def insertion_sort(arr):
    # função com insertion

# chamada da função bubble sort
bubble_sort(vetor_bubble)
print(bubble_sort(vetor_bubble))
bubble_time = time.time()
print("Tempo de execução do algoritmo bubble_sort = {:.2f}s".format(bubble_time - inicio_time))

# chamada da função selection sort
selection_sort(vetor_selection)
print(selection_sort(vetor_selection))
selection_time = time.time()
print("Tempo de execução do algoritmo selection_sort = {:.2f}s".format(selection_time - inicio_time))

# chamada da função insertion sort
inserton_sort(vetor_insertion)
print(insertion_sort(vetor_insertion))
insertion_time = time.time()
print("Tempo de execução do algoritmo selection_sort = {:.2f}s".format(insertion_time - inicio_time))
