print('Passagem de ônibus')
x = float(input('Digite a distância em Km: '))
if x <= 200:
    y = x * 0.5
else:
    y = x * 0.45
print(f'Sua passagem custará R${y:.2f}\n'
      'Boa viagem')
