from time import sleep

o = 0
x = float(input('Digite o 1º valor: '))
y = float(input('Digite o 2º valor: '))

while not o == 5:
    M = 0
    o = int(input('[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Novos números\n'
                  '[5] Sair do programa\n'
                  ''))
    if o == 1:
        print(f'A soma entre {x} e {y} é {x + y:.2f}')
    elif o == 2:
        print(f'A multiplicação entre {x} e {y} é {x * y:.2f}')
    elif o == 3:
        if y > x:
            M = y
            print(f'O maior valor entre {x} e {y} é {M:.2f}')
        elif x > y:
            M = x
            print(f'O maior valor entre {x} e {y} é {M:.2f}')
        else:
            print(f'Não há maior, os dois são iguais')
    elif o == 4:
        x = float(input('Digite o 1º valor novamente: '))
        y = float(input('Digite o 2º valor novamente: '))
    elif o == 5:
        print('Finalizando...\n'
              'Volte sempre!')
    else:
        print('Opção inválida. Tente novamente')
    print('=-' * 10)
    sleep(1.5)
