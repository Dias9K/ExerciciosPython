import timeit


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

vetor = [128, 955, 695, 446, 255, 812, 818, 499, 915, 444, 806, 870, 775, 19, 470, 779, 971, 995, 383, 535, 516, 252, 222, 595, 604, 707, 339, 918, 877, 895, 284, 613, 43, 868, 4, 85, 139, 826, 730, 612, 973, 932, 332, 249, 501, 258, 140, 682, 360, 753, 432, 119, 150, 100, 289, 265, 776, 531, 951, 601, 587, 854, 650, 954, 206, 490, 505, 662, 990, 891, 711, 443, 909, 687, 473, 38, 353, 876, 758, 298, 983, 135, 864, 247, 83, 839, 618, 215, 157, 296, 729, 795, 438, 680, 426, 279, 267, 186, 548, 539, 1, 571, 270, 419, 220, 874, 836, 847, 745, 862, 344, 62, 311, 991, 616, 281, 666, 13, 355, 126, 277, 440, 228, 968, 145, 459, 224, 924, 487, 497, 176, 20, 287, 626, 894, 881, 369, 42, 208, 297, 669, 820, 999, 926, 790, 379, 430, 739, 708, 30, 778, 764, 469, 929, 495, 485, 749, 673, 634, 191, 358, 410, 860, 475, 325, 964, 534, 91, 962, 36, 913, 71, 256, 581, 725, 597, 815, 507, 151, 838, 239, 645, 114, 315, 520, 108, 907, 235, 10, 697, 748, 582, 543, 542, 789, 704, 834, 500, 245, 989, 429, 798, 549, 404, 283, 515, 761, 493, 386, 392, 741, 288, 314, 101, 556, 655, 316, 945, 118, 338, 184, 232, 445, 712, 538, 377, 427, 34, 58, 900, 122, 142, 115, 60, 703, 451, 972, 422, 642, 431, 850, 305, 699, 172, 433, 833, 468, 472, 226, 805, 8, 635, 819, 559, 366, 18, 354, 681, 875, 623, 551, 244, 26, 278, 21, 692, 933, 211, 347, 577, 196, 149, 911, 193, 95, 253, 504, 343, 302, 216, 340, 893, 205, 182, 593, 174, 416, 934, 116, 202, 804, 566, 209, 794, 676, 484, 192, 986, 628, 746, 23, 246, 936, 513, 767, 773, 395, 46, 455, 852, 65, 842, 81, 439, 70, 179, 365, 614, 905, 61, 53, 589, 829, 120, 25, 553, 511, 537, 578, 694, 855, 333, 486, 963, 254, 910, 978, 544, 867, 514, 646, 970, 822, 463, 127, 896, 807, 603, 434, 648, 136, 334, 809, 498, 617, 782, 791, 550, 237, 591, 250, 359, 561, 981, 546, 351, 476, 185, 372, 622, 786, 75, 529, 547, 735, 557, 733, 309, 851, 861, 167, 890, 957, 190, 48, 908, 263, 407, 965, 389, 275, 201, 724, 39, 610, 373, 64, 800, 848, 457, 106, 54, 342, 996, 563, 143, 969, 160, 335, 517, 866, 462, 816, 938, 110, 482, 52, 306, 313, 238, 382, 15, 328, 787, 530, 390, 229, 274, 180, 801, 738, 388, 865, 975, 381, 260, 906, 803, 644, 992, 583, 569, 846, 837, 175, 558, 357, 159, 590, 454, 919, 840, 887, 436, 717, 927, 527, 988, 134, 607, 144, 9, 387, 674, 417, 796, 541, 400, 477, 45, 327, 362, 636, 857, 552, 994, 117, 661, 632, 194, 124, 133, 832, 714, 922, 718, 824, 731, 97, 976, 105, 921, 950, 941, 828, 14, 762, 398, 928, 757, 889, 961, 33, 394, 985, 792, 269, 22, 672, 189, 496, 756, 946, 849, 408, 310, 519, 802, 930, 580, 736, 170, 488, 385, 715, 599, 138, 259, 825, 221, 602, 156, 732, 917, 240, 914, 903, 998, 121, 944, 780, 96, 966, 727, 312, 679, 783, 709, 361, 292, 414, 772, 755, 873, 197, 974, 50, 223, 508, 629, 594, 424, 631, 402, 90, 720, 2, 567, 148, 72, 769, 608, 545, 649, 447, 346, 303, 685, 368, 177, 853, 411, 879, 103, 5, 35, 647, 880, 0, 489, 979, 435, 952, 935, 659, 102, 688, 624, 425, 678, 78, 817, 453, 710, 378, 742, 555, 341, 195, 811, 696, 705, 163, 293, 212, 937, 948, 606, 524, 620, 69, 47, 88, 86, 481, 51, 810, 774, 763, 643, 37, 73, 181, 132, 984, 460, 367, 280, 797, 956, 653, 28, 784, 1000, 884]


tempo_bubble, resultado_bubble = medir_tempo(bubble_sort, vetor)
print(f"Tempo de execução Bubble Sort: {tempo_bubble:.5f} segundos")
print("Array ordenado (Bubble Sort):", resultado_bubble)

tempo_selection, resultado_selection = medir_tempo(selection_sort, vetor)
print(f"Tempo de execução Selection Sort: {tempo_selection:.5f} segundos")
print("Array ordenado (Selection Sort):", resultado_selection)

tempo_insertion, resultado_insertion = medir_tempo(insertion_sort, vetor)
print(f"Tempo de execução Insertion Sort: {tempo_insertion:.5f} segundos")
print("Array ordenado (Insertion Sort):", resultado_insertion)

tempo_quicksort, resultado_quicksort = medir_tempo(quicksort, vetor)
print(f"Tempo de execução Quick Sort: {tempo_quicksort:.5f} segundos")
print("Array ordenado (Quick Sort):", resultado_quicksort)