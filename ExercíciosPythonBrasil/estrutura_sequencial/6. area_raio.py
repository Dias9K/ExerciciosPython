# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

# formúla pra calcular área de um raio - raio elevado ao quadrado, multiplicado por PI

raio_circulo = float(input("Digite o raio do seu círculo: "))
area = raio_circulo**2 * math.pi

print(f"A área do seu círculo é: {area}")
