# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado para que sua área seja calculada: "))
area = lado ** 2  # lado ELEVADO a 2
print(f"Sua área é: {area}")
print(f"O dobro da sua área é: {area * 2}")
