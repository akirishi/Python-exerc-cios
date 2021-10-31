m = 0
x = 0
v = 0
n1 = ''
y = int(input('Quantas pessoas vão ser analisada?: '))
for c in range(1, y + 1):
    print(f'----- {c}º PESSOA -----')
    n = str(input('Digite seu nome: ')).strip().lower().title()
    i = int(input('Digite sua idade: ').strip())
    s = str(input('sexo [M/F]: ').strip().lower())
    m += i
    if c == 1 and s == 'm':
        v = i
        n1 = n
    if s == 'm' and s == 'm':
        v = i
        n1 = n
        if i > v:
            n1 = n
            v = i

print(f'A média de idades é {m / c}')
if x == 0:
    print('Nenhuma mulher tem menos de 20 anos')
elif x == 1:
    print('1 mulher tem menos de 20 anos')
else:
    print(f'{x} mulheres já fizeram 20 anos')
print(f'O homem mais velho é {n} e tem {v} anos')
