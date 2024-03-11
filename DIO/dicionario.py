"""Dicionários são conjuntos não ordenados de pares com chaves e valores. As chaves são únicas em uma dada instância
 do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave: valor separado por
 vírgulas."""
# pessoa = {"nome": "Gabriel", "idade": 23}  (é a mesma coisa que essa declaração de baixo)

pessoa = dict(nome="Gabriel", idade=23)  # dict() é o construtor da classe de dicionários
pessoa["telefone"] = "85738064"  # atribuindo um novo par no dicionário

print(pessoa["nome"])  # acessando um valor do dicionário colocando a sua chave
pessoa["nome"] = "Bruna"  # atribuindo um novo valor a chave "nome"
print(pessoa)

# Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um
# objeto imutável como (strings e números).

contatos = {
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "4002-8922"},
    "bruna@gmail.com": {"nome": "Bruna", "telefone": "2004-2289"},
}  # dicionários aninhados. no dicionário "contatos" está sendo armazenado outro dicionário contendo as
# chaves de nomes e telefones dos usuários
contatos["bruna@gmail.com"]["idade"] = "22"  # atribuindo novo valor dentro de um dicionário aninhado
print(contatos["gabriel@gmail.com"]["telefone"])
print(contatos["bruna@gmail.com"]["idade"])
print(contatos["bruna@gmail.com"])
print("iterando dicionários".center(60, "="))
# for chave in contatos:
#     print(chave, contatos[chave])

for chave, valor in contatos.items():  # TODO entendi nada, preciso rever isso
    print(chave, valor)

print("testando métodos da classe".center(60, "="))
# {}.clear limpa todos os valores do dicionário
# {}.copy faz uma cópia do dicionário

# {}.fromkeys
fromkeys = dict.fromkeys(["nome", "telefone"], "vazio")  # usado para CRIAR um novo dicionário VAZIO,
# OU com valores atribuidos. primeiro coloca uma lista das chaves que serão referenciadas e depois atribuir ou não um
# valor padrão para elas, do contrário, o valor "none" é atribuído
print(fromkeys)

# {}.get
print(contatos.get("gabrel@gmail.com", "chave não encontrada"))  # o método é utilizado para procurar uma chave
# existente no dicionário, e se essa chave não for encontrada, um valor "default" será retornado
print(contatos.get("gabriel@gmail.com", {}).get("telefone", {}))
# usar dessa forma em caso de dicionários aninhados

# {}.items
print(contatos.items())  # retorna todos as chaves com valores dentro de um dicionário, sendo aninhado ou não

# {}.keys
print(contatos.keys())  # retorna todas as chaves dentro de um dicionário, mas se houverem dicionários aninhados eles
# não serão mostrados, apenas as chaves da "primeira camada"

# {}.pop
print(contatos.pop("gabriel@gmail.co", "chave não encontrada"))  # remove do dicionário a chave especificada e os
# seus valores
print(contatos.keys())
# também é possível informar um valor default, caso a chave especificada não seja encontrada

# {}.popitem
print(f"removi isso {contatos.popitem()}")  # remove um item ALEATÓRIO do dicionário
print(contatos.keys())

# {}.setdefault
console = {"nome": "xbox", "telefone": "360"}
console.setdefault("nome", "ps3")  # procura uma chave e se ela existir, será mantido o seu valor atual
console.setdefault("idade", "12")  # se a chave informada não for encontrada no dicionário, ela será criada e o valor
# informado será atribuido a ela
print(console)

# {}.update
contatos.update({"gabriel@gmail.com": {"nome": "Gabigol"}})  # sobreescreve as chaves com os valores informados
contatos.update({"joao@gmail.com": {"nome": "João", "telefone": "3322-8181"}})  # se a chave informada não existir,
# uma nova chave será criada com os valores informados
print(contatos)

# {}.values
print(contatos.values())  # retorna todos os valores dentro de um dicionário

# in
resultado = "gabriel@gmail.com" in contatos  # verifica se a chave informada contém no dicionário
resultado2 = "telefone" in contatos["gabriel@gmail.com"]  # utilizando um dicionário aninhado e fazendo a verificação
# com a chave informada
print(resultado)
print(resultado2)

# del
del contatos["joao@gmail.com"]["telefone"]
# remove uma chave específica do dicionário, o mesmo também se aplica aos dicionários aninhados, sendo necessário
# informar a sua outra chave
del contatos["gabriel@gmail.com"]
print(contatos)
