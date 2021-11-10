from random import randint

num = list()

while True:
    x = randint(0, 20)
    if x in num:
        print(f'Valor duplicado! {x} não pode ser adicionado')
    else:
        num.append(x)
        print(f'Valor {x} adicionado com sucesso!')
    opt = str(input('Continuar? [S/N]: ')).upper().strip()
    if opt == 'N':
        break
print(f'Os valores únicos digitados foram {num.sort()}')
