print('Casas decimis')

x = int(input('Digite um número: '))

print(f'Unidade:{x // 1 % 10}'
      f'Dezena:{x // 10 % 10}'
      f'Centena:{x // 100 % 10}'
      f'Milhar:{x // 1000}')
