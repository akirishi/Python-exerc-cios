M = 0
m = 0
c1 = 0

x = int(input('Quantos peso serão analisados?: '))
for c in range(1, x + 1):
    p = float(input(f'Digite o peso da {c}º pessoa: '))
    c1 = c
    if c == 1:
        M = p
        m = p
    else:
        if p > M:
            M = p
        if p < m:
            m = p

print(f'O maior peso entre os {c1} valores digitados é {M}Kg\n'
      f'e o menor é {m}Kg')
