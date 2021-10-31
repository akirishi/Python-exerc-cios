from time import sleep
print('Financiamento da casa propria')
x = float(input('Digite o valor da casa: '))
y = float(input('Digite o seu salário: '))
z = int(input('Em quantos anos deseja parcelar?: '))
print('=-='*20)
print('Calculando...')
print('=-='*20)
sleep(3)
y1 = y * 0.3
z1 = x / (z * 12)
if y1 > z1:
    print(f'Você tera de pagar R${z1:.2f} durante {z * 12} messes')
else:
    print('Infelizmente você não pode financiar essa casa')
print('---end---')
