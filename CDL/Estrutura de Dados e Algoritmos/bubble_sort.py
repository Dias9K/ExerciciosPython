

def bubble_sort(arr):
    # percorrendo todos os elemetos do array
    for i in range(len(arr)):
        # últimos i elementos já estão no lugar certo
        for j in range(0, len(arr) - i - 1):
            # troca se o elemento encontrado for maior que o próximo elemento
            if arr[j] > arr[j + i]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# exemplos
arr = [66, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
