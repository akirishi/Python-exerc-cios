from datetime import date

y = date.today().year
z = 0
z1 = 0
z2 = 0
c1 = 0
for c in range(1, 8):
    x = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    c1 = c
    if y - x < 21:
        z += 1
    elif y - x < 60:
        z1 += 1
    else:
        z2 += 1
print(f'entre essas {c1} pessoas\n'
      f'{z} são jovens\n'
      f'{z1} entre são adultos\n'
      f'e {z2} são idosos')
