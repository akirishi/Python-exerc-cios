from random import randint

num = []
x = y = 0
maior_p = []
menor_p = []

for cont in range(1, 21):
    num.append(randint(1, 10))

for c, v in enumerate(num):
    if c == 1:
        x = v
        y = v
    else:
        if v > x:
            x = v
            maior_p.append(c)
        elif v < y:
            y = v
            menor_p.append(c)

print(f'''
Dentro da lista de números há {len(num)} valores
  O maior valor encontrado foi {x} nas posições {maior_p},
E o menor valor encontrado foi {y} nas posições {menor_p}.
''')
