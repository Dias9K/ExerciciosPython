## Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))
nota4 = float(input("Digite o valor da quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A sua média é: {media}" )

media_string = str(media)
print(type(media_string))
## testando a conversão de tipos