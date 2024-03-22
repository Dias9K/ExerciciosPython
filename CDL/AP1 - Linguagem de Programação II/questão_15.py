# Questão 15 – (0,75 pontos)
# Desenvolva  um gerador  de  tabuada,  capaz de  gerar  a  tabuada  de  qualquer  número  inteiro
# entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve
# ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50.

multiplicando = int(input("Escolha um número entre 1 a 10 para ver a sua tabuada: "))
multiplicador = 1

while multiplicador <= 10:
    produto = multiplicando * multiplicador
    print(f"{multiplicando} x {multiplicador} = {produto}")
    multiplicador = multiplicador + 1
