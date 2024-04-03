import math

matriz = [[1, 20],
          [20, 30]]

media = 0

for i in range(2):
    for j in range(2):
        media = matriz[i][j] + media

media = media/6

print(f"A média dos elementos é = {math.ceil(media)}")
