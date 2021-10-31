print('-'*30)
print(f'{"Banco intergalático":^30}')
print('-'*30)

x = int(input('Quanto deseja sacar?: '))

n50 = x // 50
n20 = (x - (n50*50)) // 20
n10 = (x - (n50*50) - (n20*20)) // 10
n1 = (x - (n50 * 50) - (n20*20) - (n10*10))//1

print(f'Total de {n50} cédulas de R$50\n'
      f'Total de {n20} cédulas de R$20\n'
      f'Total de {n10} cédulas de R$10\n'
      f'Total de {n1} cédulas de R$1')
print('-'*30)
print('Volte sempre!!')

