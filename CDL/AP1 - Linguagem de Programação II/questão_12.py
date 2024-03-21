# Questão 12 – (0,75 pontos)
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
# multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
# de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
# os dados do programa com as mensagens adequadas

peso_peixes = float(input("Digite a quantidade de quilos em peixes que João fisgou em sua pesca diária: "))

if peso_peixes > 50.0:
    excesso = peso_peixes - 50.0  # atribuído apenas caso ele ultrapasse o limite de 50kg
    print(f"João ultrapassou {excesso:.2f}kg na sua pesca e foi multado!")
    valor_multa = 4.0 * excesso
    print(f"O valor da sua multa é = R${valor_multa:.2f}!")
else:
    print("João não deve pagar o valor da multa pois não excedeu o peso da sua pesca!")
