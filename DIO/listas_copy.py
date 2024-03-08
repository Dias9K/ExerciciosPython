# .copy()
lista1 = [1, "string", [10, 40, 80]]
lista2 = lista1.copy()  # copia a todos os elementos da lista
print(
    id(lista1), id(lista2)
)  # comprovando que são duas instâncias diferentes, mas com os mesmos elementos
lista2[0] = 10
print(lista1)
print(lista2)

# .count()
frutas = ["laranja", "morango", "limão", "laranja", "banana"]
print(frutas.count("laranja"))  # retorna quantas vezes um elemento se repete na lista
print(frutas.count("morango"))

# .extend()
linguagens = ["python", "java"]
print(linguagens)
linguagens.extend(["js", "c", "c#"])  # acrescenta uma outra lista em uma já existente
print(linguagens)
