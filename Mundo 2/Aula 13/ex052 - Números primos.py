print('Números primos')

x = int(input('Digite um número: '))
d = 0
for c in range(1, x + 1):
    if x % c == 0:
        d += 1
if d > 2:
    print('Esse número não é primo')
else:
    print('Esse número é primo')