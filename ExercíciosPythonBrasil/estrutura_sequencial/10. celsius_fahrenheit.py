# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 1.8) + 32

# %.1f igual em C para formatar um número, mas a representação da variável, é utilizado o % também
print("A temperatura convertida em graus Fahrenheit é: %.1f" % fahrenheit)
