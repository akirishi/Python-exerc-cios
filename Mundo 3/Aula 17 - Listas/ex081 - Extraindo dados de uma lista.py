from random import randint

x = list()
val = int(input('Quantos números vão ser análisados?: '))

for c in range(0, val):
    x.append(randint(0, 10))
    for num in x:
        if val == 5:
            pos = num


print(f'''
Nesta lista há {len(x)} valoes,
a lista em ordem decrescente é {x.sort(reverse=True)}
''')
if 5 in x:
    print(f'O valor 5 está na lista, na posição {pos}')
else:
    print('Não encontrei o valor 5 nesta lista')
