def sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                arr[j], arr[min_idx] = arr[min_idx], arr[j]
            print(arr)


vetor = [412, 412, 500, 213, 123, 0, 150, 20, 203, 13, 2, 3, 20, 3, 20, 3, 20, 302, 3203, 1223, 204, 1024]
sort(vetor)
