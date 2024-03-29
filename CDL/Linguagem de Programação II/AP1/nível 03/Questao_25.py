#Questão 25
#Gabriel Levi Lima Rodrigues
#Impporta a biblioteca calendario
import calendar
import datetime
'''---------------------------------------------------------------------------'''
print('=' * 10,'Banco Tabajara', '=' * 10)
titular = input('Nome do Depositante: ')
data_deposito_str = input('Informe a data de deposito (Formato: dd/mm/aaaa):')
deposito = float(input('Digite o valor do depósito inicial: R$'))
tx_juros = float(input('Informe a taxa de juros mensal (em %): '))
'''---------------------------------------------------------------------------'''
# Tratamento da data de deposito
try:
    data_deposito = datetime.datetime.strptime(data_deposito_str, '%d/%m/%Y')
    print("Data de depósito convertida com sucesso:", data_deposito)
except ValueError:
    print('Formato de data inválido. Por favor, insira a data no formato correto.')
    exit()
'''---------------------------------------------------------------------------'''
#Verifica se todos os caracteres da variavel titlar são letras
if not titular.replace(' ', '').isalpha():
    print('Por favor, insira apenas letras para o seu nome do depositante.')
    exit()
'''---------------------------------------------------------------------------'''
juros_decimal = tx_juros / 100
saldo = deposito
meses = 24
anos = meses // 12
meses_restante = meses % 12
'''---------------------------------------------------------------------------'''
print('=== * Extrato * ===')
for mes in range (1, meses + 1):
    juros = saldo * juros_decimal
    saldo += juros
    dias_do_mes = calendar.monthrange(data_deposito.year, data_deposito.month)[1]
    data_deposito += datetime.timedelta(days = dias_do_mes)
    print('{} - Saldo: R$ {:.2f}'.format(data_deposito.strftime('%d/%m/%Y'), saldo))

juros_total = saldo - deposito
'''---------------------------------------------------------------------------'''
# Exibir Resultado
print('=' * 50)
print('=== * Banco Tabajara * ===')
print('Depositante: {}'.format(titular))
print('Deposito inicial: R${:.2f}'.format(deposito))
print('Total ganho com juros: R${:.2f}'.format(juros_total))
print('Saldo atual: R${:.2f}'.format(saldo))
print('=== Consulta Encerrada! === ')
# Gabriel Levi Lima Rodrigues