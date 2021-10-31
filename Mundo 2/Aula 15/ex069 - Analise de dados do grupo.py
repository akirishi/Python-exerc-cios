from time import sleep

fim = ''
H = m = M = 0

while True:
    print('-' * 30)
    print(f'{"Cadastre uma pessoa":^30}')
    print('-' * 30)
    s = ''
    i = int(input('Digite sua idade'))
    if i >= 18:
        M += 1
    while not (s == 'M' or s == 'F'):
        s = str(input('Sexo [M/F]: ').upper().strip()[0])
        if s == 'M':
            H += 1
    if s == 'F' and i <= 20:
        m += 1
    fim = str(input('Fim? [S/N]: ').upper().strip()[0])
    if 'S' in fim:
        break
print('-'*30)
print('Analizando...')
print('-'*30)
sleep(1)

print(f'{M} pessoas tem mais de 18 anos\n'
      f'{H} homens foram cadastrados\n'
      f'{m} mulheres tem menos de 20 anos')
