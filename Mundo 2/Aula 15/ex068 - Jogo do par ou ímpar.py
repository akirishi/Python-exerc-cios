from random import randint
from time import sleep

v = 0

print('-' * 20)
print('Vamos brincar\n'
      'Par ou Ímpar')
print('-' * 20)
sleep(1)

while True:
    o = str(input('Par ou ímpar[P/I]: ').strip().upper()[0])
    p1 = int(input('Digite um número: '))
    com = randint(0, 10)
    s = p1 + com
    retry = ''
    if o == 'P':
        if s % 2 == 0:
            print(f'O computador jogou {com}\n'
                  f'e você jogou {p1}\n'
                  'TSC... Você venceu...\n'
                  'Revance!!')
            v += 1
        elif s % 2 != 0:
            print(f'O computador jogou {com}\n'
                  f'e você jogou {p1}\n'
                  'Você perdeu\n'
                  'GAME OVER!\n'
                  'MWAHAHAHAHAHA')
            retry = str(input('Tentar novamente?\n'
                              '[S/N]: ').strip().upper()[0])
            if retry == 'N':
                break
    elif o == 'I':
        if s % 2 != 0:
            print(f'O computador jogou {com}\n'
                  f'e você jogou {p1}\n'
                  'TSC... Você venceu...\n'
                  'Revance!!')
            v += 1
        elif s % 2 == 0:
            print(f'O computador jogou {com}\n'
                  f'e você jogou {p1}\n'
                  'Você perdeu\n'
                  'GAME OVER!\n'
                  'MWAHAHAHAHAHA')
            retry = str(input('Tentar novamente?\n'
                              '[S/N]: ').strip().upper()[0])
            if retry == 'N':
                break
if v == 0:
    print('Você não ganhou nenhuma!')
elif v == 1:
    print('Você ganhou apenas 1 vez')
else:
    print(f'Voce ganhou {v} vezes!')
