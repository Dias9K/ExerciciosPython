# Questão 19 – (1 ponto)
# Gabriel Levi Lima Rodrigues
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
# situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input('Informe em metros quadrados da área a ser pintada: '))

'''Formula para calcular a quantidade de tinta necessaria'''
tinta = area / 6

'''Formulas para calcula os dados solicitatos de acordo com a pergunta. 
    Galões de 18l e 3,6l'''
lata = math.ceil(tinta / 18)
galao = math.ceil(tinta / 3.6)

'''Calcular o preço total para comprar da lata'''
preco_lata = lata * 80

'''Calcular o preço total para comprar em galão'''
preco_galao = galao * 25

'''Mistura economica de lata e galão'''
mistura_lata = math.ceil(tinta / 18)
mistura_galao = math.ceil((tinta % 18) / 3.6)

value_tot_mistura = (mistura_lata * 80) + (mistura_galao * 25)

# Impressão de resultados
print('======== * Calculo Base em Lata * ======== ')
print('Para pintar uma área de {} m²: '.format(area))
print('Quantidade latas: {}'.format(lata))
print('Preço Total: R${:.2f}'.format(preco_lata))
print(50 * '=', '\n')

print('======== * Calculo Base em Galão * ======== ')
print('Para pintar um área de {} m²:'.format(area))
print('Quantidade de Galoes: {}'.format(lata))
print('Preço Total: R${:.2f}'.format(preco_galao))
print(50 * '=', '\n')

print('======== * Calculo Base da Mistura da Lata com Galão * ======== ')
print('Para pintar um área de {} m²:'.format(area))
print('Quantidade de Latas: {}'.format(mistura_lata))
print('Qunatidade de Galão: {}'.format(mistura_galao))
print('Preço Total: R${:.2f}'.format(value_tot_mistura))
print(50 * '=', '\n')
# Gabriel Levi Lima Rodrigues
