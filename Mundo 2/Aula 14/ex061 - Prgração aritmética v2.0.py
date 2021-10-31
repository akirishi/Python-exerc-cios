c = 0
c1 = 0
print('10 primeiros termos da PA')
print('=-'*13)
x = int(input('Digite o primeiro termo: '))
y = int(input('Digite a razão: '))
z = 10

while c1 < z:
    print(f'{x}', end='')
    print(' → ' if c1 < 9 else '', end='')
    x += y
    c1 += 1
