print('Gerador de PA')
print('=-'*13)
c = 0
x = float(input('Digite o primeiro termo: '))
y = float(input('Digite a razão: '))
z = int(input('Quantos termos?: '))

while c < z:
    print(f'{x}', end='')
    print(' → ' if c < z - 1 else ' ...', end='')
    x += y
    c += 1
    if c >= z:
        if z != 0:
            z += int(input('\nQuar mais quantos termos: '))
print(f'Foram {c} termos mostrados\n'
      'Acabou')
