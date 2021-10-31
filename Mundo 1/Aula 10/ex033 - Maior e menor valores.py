x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digire o terceiro número: '))

m = int(x)
if y < x < z:
    m = y
if z < x < y:
    m = z
print(f'O menor é {m}')
M = int(x)
if y > x > z:
    M = y
if z > x > y:
    M = z
print(f'O maior é {M}')