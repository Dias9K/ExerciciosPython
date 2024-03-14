# a palavra reservada "def" serve como um identificador para o interpretador saber que aquela declaração se trata de
# uma função
def ola_funcao():
    print("olá, função!")


def ola_pessoa():
    nome = input("Digite o seu nome: ")
    print(f"Olá, {nome.capitalize()}, meu amigo(a)")


def ola_pessoa2(nome="Anônimo"):
    print(f"Olá, {nome.capitalize()}, meu amigo(a)")


# def ola_pessoa(nome):
#     print(f"Olá, {nome}, meu amigo(a)")


ola_funcao()
# ola_pessoa()
ola_pessoa2("teste".capitalize())


def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


print(antecessor_sucessor(10))


def soma_numeros(numeros):
    return sum(numeros)


print(soma_numeros([1, 2, 3, 4, 5]))


def func3():
    print("olá mudo!")  # quando uma função em Python não tem a instrução return, ela retorna None por padrão.


print(func3())


def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido : {marca}, {modelo}, {ano}, {placa}")


# sintaxe porca que permite dados de qualquer tipo serem inseridos sem nenhuma restrição

salvar_carro(1, 2, 3, 4)
