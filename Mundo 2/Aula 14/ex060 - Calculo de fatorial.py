x = int(input('Digite um número: '))
f1 = 1

print(f'Calculando {x}! = ', end='')
for f in range(x, 0, -1):
    f1 *= f
    print(f'{f}', end='')
    print(' x ' if f > 1 else ' = ', end='')
print(f'{f1}')
