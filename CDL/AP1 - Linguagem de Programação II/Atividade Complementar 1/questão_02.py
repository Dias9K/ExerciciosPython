# Questão 02 - ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO E VERIFIQUE SE É OU NÃO UM NÚMERO PRIMO. PARA FAZER ESTA
# VERIFICAÇÃO, CALCULE O RESTO DA DIVISÃO DO NÚMERO POR 2 E DEPOIS POR TODOS OS NÚMEROS ÍMPARES ATÉ O NÚMERO LIDO. SE
# O RESTO DE UMA DESTAS DIVISÕES FOR IGUAL A ZERO, O NÚMERO NÃO É PRIMO. OBSERVE QUE O 0 E 1 NÃO SÃO PRIMOS E QUE 2
# É O ÚNICO NÚMERO PRIMO QUE É PAR.

numero = int(input("Digite um número inteiro para verificar se ele é primo ou não: "))

if numero <= 1:
    print("O número não é primo.")
elif numero == 2:
    print("O número 2 é o único número primo que é par.")

elif numero % 2 == 0:
    print("O número não é primo.")
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            print("O número não é primo")
            break
    else:
        print("O numero é primo")

'''
https://python.nilo.pro.br/exercicios3/capitulo%2005/exercicio-05-23.html
def eh_primo(n):  # Define uma função chamada 'eh_primo' que recebe um argumento 'n'.
    if n < 2:  # Se 'n' for menor que 2,
        return False  # retorna 'False'. Isso porque números menores que 2 não são primos.
    if n == 2:  # Se 'n' for igual a 2,
        return True  # retorna 'True'. Isso porque 2 é um número primo.
    if n % 2 == 0:  # Se 'n' for divisível por 2 (ou seja, se 'n' for par),
        return False  # retorna 'False'. Isso porque nenhum número par maior que 2 pode ser primo.
    i = 3  # Define uma variável 'i' e atribui o valor 3 a ela.
    while i * i <= n:  # Enquanto o quadrado de 'i' for menor ou igual a 'n',
        if n % i == 0:  # se 'n' for divisível por 'i',
            return False  # retorna 'False'. Isso porque 'n' tem um divisor além de 1 e ele mesmo, então 'n' não é primo.
        i += 2  # Incrementa 'i' em 2. Isso efetivamente verifica apenas os números ímpares como possíveis divisores.
    return True  # Se nenhum divisor foi encontrado, retorna 'True'. Isso significa que 'n' é primo.


numero = int(input(
    "Digite um número: "))  # Solicita ao usuário que digite um número e converte a entrada do usuário para um inteiro.
if eh_primo(numero):  # Se o número for primo (ou seja, se a função 'eh_primo' retornar 'True'),
    print(f"{numero} é um número primo.")  # imprime que o número é primo.
else:  # Se o número não for primo (ou seja, se a função 'eh_primo' retornar 'False'),
    print(f"{numero} não é um número primo.")  # imprime que o número não é primo.
'''
