from random import randrange
from time import sleep

print(f'{" Lojas do Carvalho ":=^40}')
x = float(input('Digite o valor do produto: R$'))
y = int(input('Escolha a forma de pagamento:\n'
              '[1] -  À vista dinheiro / Cheque.\n'
              '[2] - Cartão.\n'
              '[3] - 2x no cartão.\n'
              '[4] - 3x ou mais no cartão.\n'
              ''))

print(f'{"":=^15}'
      'Calculando...'
      f'{"":=^15}')
sleep(randrange(1, 4))

if y == 1:
    print('Nessa opção você ganha 10% de desconto.\n'
          f'O valor de R${x:.2f} passa a ser R${x - (x * 0.1):.2f}.')
elif y == 2:
    print('Nessa opção você ganha 5% de desconto.\n'
          f'O valor de R${x:.2f} passa a ser R${x - (x * 0.05):.2f}.')
elif y == 3:
    print(f'O valor a ser pago é de R${x:.2f}'
          f' em 2 parcelas de R${x / 2:.2f}.')
elif y == 4:
    z = int(input('Quantas parcelas?: '))
    print('Nessa opção você tera 20% de juros.'
          f'O valor de R${x:.2f} passa a ser R${x * 1.2:.2f},\n'
          f'e sera pago em {z} parcelas de R${(x * 1.2) / z:.2f}.')
else:
    print('Código inválido, reinicie a página.')
