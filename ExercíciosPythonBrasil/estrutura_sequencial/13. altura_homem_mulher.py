"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7"""

while True:
    sexo = input("Digite o seu sexo\n[M] - Masculino\n[F] - Feminino\n")
    if sexo[0].lower() != "m" and sexo[0].lower() != "f":
        print("Sexo inválido! Digite apenas as entradas sugeridas.")
# TODO fazer dar loop apenas para retornar apenas para corrigir a opção inválida, não o código inteiro
    elif sexo[0].lower() == "m" or sexo[0].lower() == "f":
        while True:
            try:
                altura = float(input("Digite a sua altura: "))
                if sexo[0].lower() == "m":
                    print(f"O peso ideal para o sexo masculino é: {(72.7 * altura) - 58:.2f}")
                    break
                elif sexo[0].lower() == "f":
                    print(f"O peso ideal para o sexo feminino é: {(62.1 * altura) - 44.7:.3f}")
                    break
            except ValueError:
                print("Valor inválido! Digite apenas inteiros ou flutuantes.")

