# Q1 Estrutura de Dados e Algoritmos
# - Crie um vetor com 5 números;
# - Procure um número x no vetor;
# - Imprima a posição do número x;
# - Se x não for encontrado imprima -1.

num1 = int(input('DIGITE O 1 NUMERO: '))
num2 = int(input('DIGITE O 2 NUMERO: '))
num3 = int(input('DIGITE O 3 NUMERO: '))
num4 = int(input('DIGITE O 4 NUMERO: '))
num5 = int(input('DIGITE O 5 NUMERO: '))

vetor = [num1, num2, num3, num4, num5]
x = int(input(f'DIGITE UM NUMERO A SER PROCURADO NO VETOR {vetor} : '))

for i in range(len(vetor)):
    if x == vetor[i]:
        print(f'\nO NUMERO {x} FOI ENCONTRADO NA POSICAO {i}')
        break
if x != vetor[i]:
    print('O NUMERO DIGITADO NAO FOI ENCONTRADO DENTRO DO VETOR')
    print(-1)