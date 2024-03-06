""" Aluno: Gabriel Magalhães Dias
Crie um vetor que receba 50 números. Desses 50 números, 
verifique quantas vezes o número 6 foi repetido.
Calcule também a porcentagem das vezes que o número 6 se repetiu.
 """

import random

vetor = []
for i in range(50):
    vetor.append(random.randint(0, 50))  # 50 números aleatórios
print("Quantidade de números inseridos:", len(vetor))
contador = 0
for y in vetor:
    if y == 6:
        contador += 1

porcentagem = (contador * 50) / 100
print(f"Números gerados dentro do vetor:\n{vetor}")
print(f"O número 6 foi repetido {contador}x")
print(f"A porcentagem das vezes que o número 6 se repetiu é: {porcentagem}%")