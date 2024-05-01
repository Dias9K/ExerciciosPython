import random
import time

inicio_time = time.time()

# atribuição dos 1000 elementos no vetor
vetor = []
for i in range(0, 1000):
    vetor.append(random.randint(1, 1000))


def selection_sort(arr):
    # função com selection
    total = len(arr)
    for i in range(total):
        idx_min = i
        for j in range(i + 1, total):
            if arr[j] < arr[idx_min]:
                arr[j], arr[idx_min] = arr[idx_min], arr[j]
    return arr


selection_sort(vetor)
print(selection_sort(vetor))
selection_time = time.time()

print(selection_time - inicio_time)
