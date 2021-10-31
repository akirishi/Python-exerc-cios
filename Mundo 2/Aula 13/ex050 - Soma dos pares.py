print(f'{"Somando os pares":=^30}')

y = 0
z = 0
n = int(input('Quantos números vão ser somados?: '))
for c in range(1, n + 1):
    x = int(input(f'Digite um {c}º número: '))
    if x % 2 == 0:
        y += x
        z += +1
print(f'Você digitou {z} números pares e a soma deles é {y}')
