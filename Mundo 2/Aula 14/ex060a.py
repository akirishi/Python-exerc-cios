from math import factorial

terminou = False

n = int(input('Digite um número e veja seu fatorial: '))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f'{factorial(n)}')
