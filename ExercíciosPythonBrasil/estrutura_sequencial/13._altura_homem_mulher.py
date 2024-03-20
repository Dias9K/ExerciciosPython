"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7"""

sexo = input("Digite o seu sexo\n[M] - Masculino\n[F] - Feminino\n")
# TODO verificar se a entrada de sexo é válida ou não
altura = float(input("Digite a sua altura: "))

while sexo[0].lower() == "m" or sexo[0].lower() == "f":
    if sexo == "m":
        print(f"O peso ideal para o sexo masculino é: {(72.7 * altura) - 58:.3f}")
        break
    elif sexo == "f":
        print(f"O peso ideal para o sexo feminino é: {(62.1 * altura) - 44.7:.3f}")
        break
    else:
        print("Opção inválida!")