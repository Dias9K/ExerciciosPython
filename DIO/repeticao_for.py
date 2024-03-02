texto = input("Digite o seu texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=(""))
# o método upper retorna uma letra maiúscula.
# neste contexto, o método está verificando se há uma letra máiuscula
# que contenha no texto, se sim, ele retorna essa letra que tem no texto
else:
    print(texto)