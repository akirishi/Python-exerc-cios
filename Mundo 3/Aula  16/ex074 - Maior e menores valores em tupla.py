from random import randint
from time import sleep

x = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
y = z = c = 0
print('Os valores sorteados foram: ', end='')
for n in x:
    c += 1
    print(n, end='')
    if c < 5:
        print('', end=', ')
    else:
        print('', end='')
print('\nCalculando...')
sleep(randint(0, 2))
print('=-' * 20)
print(f'O maior é {max(x)}\n'
      f'O menor é {min(x)}')
print('=-' * 20)
