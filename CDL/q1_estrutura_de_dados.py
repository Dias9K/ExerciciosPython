""" Aluno: Gabriel Magalhães Dias 
 Q1 Estrutura de Dados e Algoritmos
- Crie um vetor com 5 números;
- Procure um número x no vetor;
- Imprima a posição do número x;
- Se x não for encontrado, imprima -1 """

# criação e inserção dos números no vetor
vetor_numero = []
for i in range(5):
    numeros_inseridos = int(input("Digite um numero para ser adicionado no vetor: "))
    vetor_numero.append(numeros_inseridos)
print(f"Os números inseridos foram: {vetor_numero}")

# definição do número a ser buscado e booleano para verificar se o número foi encontrado ou não
numero_procurado = int(input("Digite um número a ser procurado no vetor: "))
numero_encontrado = False

# verificações no vetor
for i in range(len(vetor_numero)): #len() retorna o número de elementos dentro do vetor
    if (numero_procurado == vetor_numero[i]):
        print(f"O número {numero_procurado} foi encontrado na posição {i} do vetor!")
        numero_encontrado = True
        break
if not numero_encontrado:
    print(f"O número {numero_procurado} não foi encontrado dentro do vetor! (-1)")