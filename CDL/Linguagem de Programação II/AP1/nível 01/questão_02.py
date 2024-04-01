# Cristian Ribeiro Calaço
# Questão 02 – (0,5 pontos)
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganha_hora = float(input('Quanto você ganha por hora?'))
horas_trabalhadas = int(input('Quantas horas você trabalha por mês:'))

salario_bruto = ganha_hora * horas_trabalhadas

print('Salário Bruto : R$ %.2f' % salario_bruto)
