from random import randint
from time import sleep

i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)

print('Vamos jogar jokenpô!')
y = str(input('Qual seu nome?: '))
x = int(input('Digite:\n'
              '[0] - Tesoura\n'
              '[1] - Pedra\n'
              '[2] - Papel\n'
              ''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print(f'{"-":-^30}\n'
      f'O computador jogou {i[c]}\n'
      f'O jogador jogou {i[x]}\n'
      f'{"-":-^30}')

if c == 0:
    if x == 0:
        print('Foi um empate!')
    elif x == 1:
        print('O jogador ganhou!\n'
              f'Parabéns {y}!')
    elif x == 2:
        print('O computador ganhou!')
    else:
        print('Jogada inválida!')
elif c == 1:
    if x == 0:
        print('O computador ganhou!')
    elif x == 1:
        print('Foi um empate!')
    elif x == 2:
        print('O jogador ganhou!\n'
              f'Parabéns {y}!')
    else:
        print('Jogada inválida!')
else:
    if x == 0:
        print('O jogador ganhou!\n'
              f'Parabéms {y}!')
    elif x == 1:
        print('O computador ganhou!')
    elif x == 2:
        print('Foi um empate!')
    else:
        print('Jogada inválida!')
