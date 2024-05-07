def bubble_sort(arr):
    # percorrendo todos os elemetos do array
    total_vetor = len(arr)
    for i in range(total_vetor):
        # últimos i elementos já estão no lugar certo
        for j in range(0, total_vetor-i-1):
            # troca se o elemento encontrado for maior que o próximo elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# exemplos
vetor = [66, 34, 25, 12, 22, 11, 90]
bubble_sort(vetor)
print(vetor)