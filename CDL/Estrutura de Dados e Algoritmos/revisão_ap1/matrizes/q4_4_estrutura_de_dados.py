# Crie um programa que crie uma matriz, com as notas de 40 alunos e devolva a
# média da turma, a maior e a menor nota.

import random

matriz_turma = []
for i in range(40):
    linha = []
    for j in range(3):
        linha.append(random.uniform(0, 10))
    matriz_turma.append(linha)
# TODO entender e continuar
# for i in range(1, 41):
#     matriz_turma.append(random.uniform(0, 10))
#
# for i in range(len(matriz_turma)):
#     print(f"{matriz_turma[i]:.2f}")
