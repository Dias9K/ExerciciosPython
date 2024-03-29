# Questão 02 - ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO E VERIFIQUE SE É OU NÃO UM NÚMERO PRIMO. PARA FAZER ESTA
# VERIFICAÇÃO, CALCULE O RESTO DA DIVISÃO DO NÚMERO POR 2 E DEPOIS POR TODOS OS NÚMEROS ÍMPARES ATÉ O NÚMERO LIDO. SE
# O RESTO DE UMA DESTAS DIVISÕES FOR IGUAL A ZERO, O NÚMERO NÃO É PRIMO. OBSERVE QUE O 0 E 1 NÃO SÃO PRIMOS E QUE 2
# É O ÚNICO NÚMERO PRIMO QUE É PAR.

numero = int(input("Digite um número inteiro para verificar se ele é primo ou não: "))

if numero < 0:
    print(f"Digite apenas números inteiros, positivos e maiores do que zero.")
elif numero == 1 or numero == 0:  # 0 e 1 não são primos
    print(f"O número {numero} não é primo.")
else:
    if numero == 2:  # 2 é o único par primo
        print("O número 2 é primo")
    elif numero % 2 == 0:  # verificando se o número é par e dizendo que não é primo
        print(f"O {numero} não é primo, apenas 2 é um número par e primo")
    else:
        primo = 3
        while primo < numero:
            if numero % primo == 0:
                break
            primo += 2
        if primo == numero:
            print(f"O {numero} é primo")
        else:
            print(f"O {numero} não é primo, pois é divisível por {primo}")  # TODO colocar todos os números divisíveis
