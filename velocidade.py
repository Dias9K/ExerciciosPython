palavra = "velocidade"

for i in range(len(palavra)):
    print(palavra[:i+1])

    '''palavra = "VELOCIDADE": Aqui, estamos definindo uma variável chamada palavra com o valor “VELOCIDADE”. for i 
    in range(len(palavra)):: Este é um loop for que percorre os índices de 0 até o comprimento da palavra (no caso, 
    10, pois “VELOCIDADE” tem 10 letras). print(palavra[:i+1]): Aqui, estamos imprimindo uma parte da palavra. O 
    trecho palavra[:i+1] pega os primeiros i+1 caracteres da palavra. Isso significa que na primeira iteração, 
    ele imprimirá apenas a primeira letra (“V”), na segunda iteração, as duas primeiras letras (“VE”), e assim por 
    diante, até a palavra completa (“VELOCIDADE”).'''