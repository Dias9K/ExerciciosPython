print('Realizado por: Gabriel Levi Lima Rodrigues')
# Leitura das duas strings
texto1 = input("Digite a primeira string: ")
texto2 = input("Digite a segunda string: ")

#Conversor para maiuscula
texto1_convert = texto1.upper()
texto2_convert = texto2.upper()

# Verificação se a segunda string ocorre dentro da primeira
posicao = texto1.find(texto2)


# Verificação do resultado e impressão
if posicao != -1:
    print(f"{texto2} encontrado na posição {posicao + 1} de {texto1}")
else:
    print(f"{texto2} não encontrado em {texto1}")