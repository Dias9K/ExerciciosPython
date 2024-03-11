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
contatos["bruna@gmail.com"]["idade"] = 22  # atribuindo novo valor dentro de um dicionário aninhado e acessando os pares
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
print(contatos.keys())  # retorna todas as chaves dentro de um dicionário, mas não se houverem dicionários aninhados

# {}.pop
print(contatos.pop("gabriel@gmail.co", "chave não encontrada"))  # remove do dicionário a chave especificada e os
# seus valores
print(contatos.keys())
# também é possível informar um valor default, caso a chave especificada não seja encontrada

# {}.popitem
print(f"removi isso {contatos.popitem()}")  # remove um item ALEATÓRIO do dicionário
print(contatos.keys())

# {}.setdefault
