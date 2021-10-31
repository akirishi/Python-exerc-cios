num = []
x = 0
while True:
    x = int(input('Digite um valor: '))
    if x in num:
        print('Valor duplicado não pode ser adicionado')
    else:
        num.append(x)
        print('Valor adicionado com sucesso!')
    y = str(input('Continuar? [S/N]: ')).upper().strip()
    if y == 'N':
        break
print(f'Os valores únicos digitados foram {num.sort()}')
