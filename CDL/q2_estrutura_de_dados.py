"""
Aluno: Gabriel Magalhães Dias
Q2 - Estrutura de Dados e Algoritmos
Um dado é lançado 50 vezes, e o seu valor correspondente
é armazenado em um vetor. Faça um programa que determine
o percentual de ocorrências do número 6 dentre esses 50 lançamentos."""

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