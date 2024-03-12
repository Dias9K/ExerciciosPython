print('==================================================')
print('================ AINDA VAI FUMAR? ================')
print('==================================================')

quantcigar = int(input('QUANTOS CIGARROS FUMADOS POR DIA: '))
years = int(input('PERÍODO EM ANOS: '))
total_mins_lost = quantcigar * 10 * (years * 365)
total_days_lost = total_mins_lost / 1440

print(f'QUANTIDADE APROXIMADA DE DIAS PERDIDOS: {total_days_lost:.2f}')