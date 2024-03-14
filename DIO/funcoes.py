# a palavra reservada "def" serve como um identificador para o interpretador saber que aquela declaração se trata de
# uma função
def ola_funcao():
    print("olá, função!")


def ola_pessoa():
    nome = input("Digite o seu nome")
    print(f"Olá, {nome}, meu amigo(a)")


# def ola_pessoa(nome):
#     print(f"Olá, {nome}, meu amigo(a)")


ola_funcao()
ola_pessoa()
