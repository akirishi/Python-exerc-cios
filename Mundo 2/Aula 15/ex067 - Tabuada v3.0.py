from time import sleep

while True:
    x = float(input('Quer ver a tabuada de qual número?\n'
                    '(Negativo para finalizar): '))
    if not x < 0:
        for c in range(1, 11):
            print(f'{x} X {c:2} = {x * c:.2f}')
    else:
        print('Finalizando...')
        print('-'*20)
        sleep(1)
        break
