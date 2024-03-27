while True:
    opcao = int(input("Escolha uma conversão\n[1] - Converter graus Celsius para graus Fahrenheit\n[2] - Converter "
                      "graus Celsius para graus Kelvin\n"))
    if opcao == 1:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print("A temperatura convertida em graus Fahrenheit é: %.1f°F" % fahrenheit)
        break

    elif opcao == 2:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        kelvin = celsius + 273.15
        print("A temperatura convertida em graus Kelvin é: %.1fK" % kelvin)
        break
    else:
        print("Opção inválida!\nEscolha uma opção correta.\n")
