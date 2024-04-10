# Crie um programa que dado um vetor, devolva 2 outros vetores com o quadrado
# e o cubo dos valores do vetor inicial.

vetor = []
quadrado = []
cubo = []
for i in range(1, 10):
    vetor.append(i)
print(vetor)

for i in vetor:
    quadrado.append(i**2)
    cubo.append(i**3)

print(quadrado)
print(cubo)
