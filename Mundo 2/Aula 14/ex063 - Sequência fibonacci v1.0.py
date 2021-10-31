print('Sequência de fibonacci')
print('=-'*25)
x = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
c = 0
print('~'*30)
print(f'{t1} → {t2} → ', end='')
while not c == x - 2:
    tn = t1 + t2
    t1 = t2
    t2 = tn
    c += 1
    print(f'{tn}', end='')
    print(' → ' if c < x - 2 else '', end='')
print(f'\nForam {c + 2} termos')
print('~'*30)
