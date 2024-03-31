# Gabriel Magalhães Dias
# Questão 11 – (0,75 pontos)
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - o produto (resultado da multiplicação) do dobro do primeiro com metade do segundo.
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.

inteiro_1 = int(input("Digite um número inteiro: "))
inteiro_2 = int(input("Digite outro número inteiro: "))
real_6 = float(input("Digite um número real: "))
dobro_inteiro_1 = inteiro_1 * 2
metade_inteiro_2 = int(inteiro_2 / 2)
triplo_inteiro_1 = inteiro_1 * 3

print(f"\nO dobro do primeiro número inteiro é = {dobro_inteiro_1}\n"
      f"A metade do segundo número inteiro é = {metade_inteiro_2}\n"
      f"Produto dos números inteiros:\n{dobro_inteiro_1} x {metade_inteiro_2} = {dobro_inteiro_1 * metade_inteiro_2}\n")

print(f"O triplo do primeiro número é = {triplo_inteiro_1}\n"
      f"O terceiro número é = {real_6}\n"
      f"Soma do triplo com o terceiro número:\n{triplo_inteiro_1} + {real_6} = {triplo_inteiro_1 + real_6}\n")
# fiz apenas o triplo do PRIMEIRO número e somei com o terceiro, se for a soma com os DOIS triplos, a correção está
# abaixo:
# print(f"Soma do triplo com o terceiro número:\n{triplo_inteiro_1} + {real_6} = {triplo_inteiro_1 + real_6 * 3}\n")

print(f"O terceiro número elevado ao cubo é = {real_6 ** 3:.2f}")
