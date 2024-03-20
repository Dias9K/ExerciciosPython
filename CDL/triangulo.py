# crie um sistema que receba valores e diga se forma um triângulo ou não
def verificar_triangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if verificar_triangulo(lado1, lado2, lado3):
    print("Os comprimentos fornecidos formam um triângulo!")
else:
    print("Os comprimentos fornecidos não formam um triângulo!")