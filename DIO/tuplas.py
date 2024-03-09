# as tuplas são basicamente iguais as listas, sua pricipal
# diferença é que essas são imutáveis, ou seja, a partir do momento que uma tupla é instanciada, qualquer alteração
# na mesma não é mais permitida
frutas = ("laranja", "morango", "limão", "banana",)  # é uma boa prática colocar uma vírgula ao final da instanciação
# de uma tupla, isso ajuda o interpretador do python a não se confundir com um parêntese de precedência em uma operação

print(frutas)

print("isso é uma tupla?", isinstance(frutas, tuple))  # retorna um booleano dizendo que a instância é ou não da classe
# que é passada no parâmetro

# sendo assim, apenas os métodos (passivos) funcionarão para essa classe, tais como:
# count(), index()
