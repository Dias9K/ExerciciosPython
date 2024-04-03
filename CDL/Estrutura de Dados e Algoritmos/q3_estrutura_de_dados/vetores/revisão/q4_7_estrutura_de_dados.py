notas = []
maior_nota = 0.0
menor_nota = 0.0
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
