"""Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados
 por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro fumado e calcule
 quantos dias de vida esse fumante perdeu. Exiba o total em dias."""

print("Olá, fumante nojento!".center(50, "="))
print("Sabia que a cada cigarro que você fuma, 10 minutos da sua vida são jogados no lixo?\n"
      "Imagine só quantos dias você já não deve ter perdido, né?")
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia?\n"))
anos_fumados = int(input("Há quantos anos você é fumante?\n"))

anos = cigarros_por_dia * (365 * anos_fumados)
minutos_perdidos = anos * 10
dias_perdidos = minutos_perdidos / 1440  # número de minutos em um dia

print(f"PARABÉNS! VOCÊ VAI MORRER {int(dias_perdidos)} DIAS MAIS CEDO!".center(50, "="))
