print('Conversor númerico')
x = int(input('Digite um número: '))
y = int(input('Digite 1 para binario\n'
              'Digite 2 para octal\n'
              'Digite 3 para hexadecimar\n'
              ''))

if y == 1:
    print(f'O número {x} convertido em binário é {bin(x)}')
elif y == 2:
    print(f'O número {x} convertido em octal é {oct(x)}')
elif y == 3:
    print(f'O número {x} convertido em hexadecimal é {hex(x)}')
