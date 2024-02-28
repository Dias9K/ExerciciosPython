# criação de listas que receberão os seus valores de acordo com o array de números
numeros = []
quadrados = []
cubos = []
max_numeros = 5

# atribuição de valores nas listas seguindo a condição da variável de máximo de números
for i in range(max_numeros):
    numeros.append(int(input("Digite os seus números: ")))
    quadrados.append(numeros[i] * numeros[i])
    cubos.append(numeros[i] * numeros[i] * numeros[i])

# saída dos elementos atribuídos nas listas
print(f"Os números inseridos foram:\n{numeros}")
print(f"Números elevados ao quadrado\n{numeros[i]*numeros[i]}")
print(cubos)

#somente com o número 2