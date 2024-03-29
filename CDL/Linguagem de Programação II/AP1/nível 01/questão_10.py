# Questão 10 – (0,5 pontos)
# Cristian Ribeiro Calaço
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num_1 = int(input('Digite o primeiro numero: '))
num_2 = int(input('Digite o segundo numero: '))

if num_1 > num_2:
    print('O primeiro número: %d, é maior' % num_1)
else:
    if num_1 == num_2:
        print('Os números são iguais')
    else:
        print('O segundo número: %d, é maior' % num_2)
