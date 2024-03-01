# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8

# %.1f igual em C para formatar um número, mas a representação da variável, é utilizado o % também
print("A temperatura convertida em graus Celsius é: %.1f" % celsius)
