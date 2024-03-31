# Gabriel Magalhães Dias
# Questão 19 – (1 ponto)
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
preco_lata_18L = 80
litros_lata = 18
preco_galao_3_6L = 25
litros_galao = 3.6

print("Color Tintas Store".center(50, "="),
      "\nSeja muito bem vindo, a nossa loja está com promoções imperdíveis para você!!")
metros_quadrados = float(input("Digite em metros quadrados a área a ser pintada: "))

# calculando as quantidades das tintas
quantidade_litros = metros_quadrados / 6
# o método math.ceil retornará um valor inteiro arredondado para o próximo número
quantidade_latas = math.ceil(quantidade_litros / litros_lata)
quantidade_galoes = math.ceil(quantidade_litros / litros_galao)
quantidade_mix_latas = int(quantidade_latas // 18)  # TODO rever esses cálculos
quantidade_mix_galoes = math.ceil((quantidade_litros % 18) / 3.6)

# calculando o valor dos casos (só latas, galões ou os dois juntos)
valor_apenas_latas = preco_lata_18L * quantidade_latas
valor_apenas_galoes = preco_galao_3_6L * quantidade_galoes
valor_mix = (quantidade_mix_latas * 80) + (quantidade_mix_galoes * 18)

print("Para aproveitar nossas promoções, é possível fazer suas compras nas seguintes modalidades:\n"
      f"\n* Comprando apenas latas de 18L\n"
      f"Quantidade de latas necessárias: {quantidade_latas}\n"
      f"Total = R${valor_apenas_latas}\n"
      f"\n* Comprando apenas galões de 3,6L\n"
      f"Quantidade de galões necessários: {quantidade_galoes}\n"
      f"Total = R${valor_apenas_galoes}\n"
      f"\n* Comprando latas e galões\n"
      f"Quantidade de latas necessárias: {quantidade_mix_latas}\n"
      f"Quantidade de galões necessários: {quantidade_mix_galoes}\n"
      f"Total = R${valor_mix}")
