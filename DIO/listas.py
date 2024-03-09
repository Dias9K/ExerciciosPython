frutas = ["laranja", "morango", "limão", "banana"]
for i in range(len(frutas)):
    print(frutas[i])  # também é possível acessar os elementos usando valores negativos no índice
# for fruta in frutas:
#     print(fruta)

letras = list("python")  # cria uma lista, onde cada letra da string é um elemento,
# se não houver argumento no método list, é criado uma lisa vazia
print(letras)
print(letras[::-1]) #espelha e inverte a ordem dos elementos

numeros = list(range(10))  # cria uma lista com o total de valores passados no range
print(numeros)

print([numero for numero in numeros if numero % 2 == 0])
# a primeira variável é um retorno, ou seja, após a verificação, ela que será retornada
# depois é feito um laço for convencional (for numero in numeros), onde todos os elementos da lista irão para a variável "numero"
# colocar ou não a condicional (if)
# de certa forma, me parece que o interpretador faz primeiro o laço for,
# depois disso ele faz a verificação da condicional e depois desse processo,
# é retornado a variável local contendo o resultado de tudo isso