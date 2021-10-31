x = c = M = m = med = 0
y = ''

while not y == 'N':
    x = int(input('Digite um número: '))
    y = str(input('Quer continuar? [S/N]').strip().upper()[0])
    med += x
    c += 1
    if c == 1:
        M = x
        m = x
    else:
        if x > M:
            M = x
        if x < m:
            m = x

print(f'{c} foram digitados e sua média é {med/c:.2f}\n'
      f'O maior valor digitado foi {M} e o menor foi {m}')
