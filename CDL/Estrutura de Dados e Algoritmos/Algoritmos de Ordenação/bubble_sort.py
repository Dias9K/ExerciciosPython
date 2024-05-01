def bubble_sort(arr):
    # percorrendo todos os elemetos do array
    total_vetor = len(arr)
    for i in range(total_vetor):
        # últimos i elementos já estão no lugar certo
        for j in range(i, total_vetor - 1):
            # troca se o elemento encontrado for maior que o próximo elemento
            if arr[j] > arr[j + i]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# exemplos
vetor = [66, 34, 25, 12, 22, 11, 90]
bubble_sort(vetor)
print(vetor)
# https://www.kabum.com.br/produto/441114/placa-de-video-pcyes-nvidia-geforce-g-210-1-gb-ddr3-pvg2101gbr364lp
