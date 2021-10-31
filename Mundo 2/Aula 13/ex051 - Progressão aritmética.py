print(f'{"10 termos de uma PA":=^50}')

x = int(input('Digite o primeiro termo: '))
y = int(input('Digite a razão: '))

for c in range(x, x + (10 * y), y):
    print(f'{c}', end=", ")
print('Fim')
