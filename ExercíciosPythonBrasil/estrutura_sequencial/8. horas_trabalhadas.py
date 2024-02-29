# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input("Digite o valor da sua hora trabalhada: "))
horas_trabalhadas = int(input("Digite a sua quantidade de horas trabalhadas por mês: "))
diaria = horas_trabalhadas*ganho_por_hora
dias_trabalhados_fevereiro = 21

print(f"Em fevereiro você ganhou R$ {dias_trabalhados_fevereiro*diaria}")