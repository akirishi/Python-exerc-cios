from random import randrange
from time import sleep

print('Vamos brincar!\n'
      'Tente adivinhar o número entre 0 e 5 que estou pensando')

print('=-' * 20)
print('Pensando...')
print('=-' * 20)
sleep(1)

x = randrange(0, 5)

y = int(input('Em que número estou pensando?: '))
print(f'Você acertou! Era {x}' if y == x else print(f'Que pena, você errou, era {x}.\nVamos denovo!'))
