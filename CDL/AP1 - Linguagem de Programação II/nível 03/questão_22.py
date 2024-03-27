# Questão 22 – (1 ponto)
# GABRIEL MAGALHÃES DIAS
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# TODO fazer usando listas ?
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já  trabalhou  com  a  vítima?"  O  programa  deve  no  final  emitir  uma  classificação  sobre  a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
# contrário, ele será classificado como "Inocente".

# função para verificar as respostas do usuário
def verifica_resposta(pergunta):
    while True:
        resposta = input(pergunta + "\n")
        if resposta.lower() == 's' or resposta.lower() == 'n':
            return resposta.lower()
        else:
            print("Resposta inválida, por favor responda com 'S' ou 'N'")


# perguntas feitas utilizando a função de verificação
perguntas = []
print("Perguntas sobre o crime (por favor, responder com 'S' ou 'N')")
perguntas.append(verifica_resposta("Telefonou para a vítima?"))
perguntas.append(verifica_resposta("Esteve no local do crime?"))
perguntas.append(verifica_resposta("Mora perto da vítima?"))
perguntas.append(verifica_resposta("Devia para a vítima?"))
perguntas.append(verifica_resposta("Já trabalhou com a vítima?"))

# conta quantas vezes o usuário respondeu as perguntas positivamente
contador_respostas = 0
for r in perguntas:
    if r == 's':
        contador_respostas += 1

# verifica a quantidade de respostas positivas do usuário e o classifica como suspeito, cúmplice, assassino ou inocente
if contador_respostas == 2:
    print(f"Suas respostas positivas foram {contador_respostas}, portanto, você é suspeito!")
elif contador_respostas > 2 and contador_respostas <= 4:
    print(f"Suas respostas positivas foram {contador_respostas}, portanto, você é cúmplice!")
elif contador_respostas == 5:
    print(f"Suas respostas positivas foram {contador_respostas}, portanto, você é assassino!")
else:
    print(f"Suas respostas positivas foram {contador_respostas}, portanto, você é inocente!")
