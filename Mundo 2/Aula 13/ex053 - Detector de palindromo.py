x = str(input('Digite uma frase: ')).strip().upper()
y = x.split()
z = ''.join(y)
i = ''

for t in range(len(z) - 1, - 1, -1):
    i += z[t]
print(f'A frase {z} ao contrario é {i}')
if z == i:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palínfromo')
