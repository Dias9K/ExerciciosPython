# Escreva um código em Python que receba, via teclado, 3 notas de um aluno, insira as notas em um vetor e imprima no
# console a maior e menor nota.

notas = []
maior_nota = 0.0
menor_nota = 10.0
for i in range(3):
    nota = float(input("Digite sua nota: "))
    notas.append(nota)

for i in notas:
    if i > maior_nota:
        maior_nota = i
print(f"A maior nota é: {maior_nota}")

for i in notas:
    menor_nota = maior_nota
    if i < menor_nota:
        menor_nota = i

print(f"A menor nota é: {menor_nota}")


'''
notas = []

for i in range(3):
    notas.append(float(input("Digite uma nota: ")))

maior_nota = notas[0]
menor_nota = notas[0]

for i in range(len(notas)):
    if notas[i] > maior_nota:
        maior_nota = notas[i]

    if notas[i] < menor_nota:
        menor_nota = notas[i]

print(f"A maior nota é {maior_nota}")
print(f"A maior nota é {menor_nota}")
'''