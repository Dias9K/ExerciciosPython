# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto (resultado da multiplicação) do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiro_1 = int(input("Digite um número inteiro: \n"))
inteiro_2 = int(input("Digite outro número inteiro: \n"))
real_3 = float(input("Digite um número real: \n"))

print(
    f"O produto do dobro do primeiro número({inteiro_1 * 2}) com metade do segundo número("
    f"{inteiro_2 / 2}) é = {(inteiro_1 * 2) + (inteiro_2 / 2)}")

print(f"A soma do tripo do primeiro número({inteiro_1 * 3}) com o terceiro número({real_3}) é "
      f"= {inteiro_1 * 3 + real_3}")

print(f"O terceiro número elevado ao cubo é = {real_3 * real_3 * real_3}")
