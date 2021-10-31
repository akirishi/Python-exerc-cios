from random import randrange
from time import sleep

print('Vamos brincar!\n'
      'Tente adivinhar o número entre 0 e 10 que estou pensando')

sleep(1)
print('=-' * 30)
print(f'{"Pensando":.^60}')
x = randrange(0, 10)
c = 0
print('=-' * 30)
sleep(1)

acertou = False
while not acertou:
    y = int(input('Digite sua tentativa: '))
    c += 1
    if x == y:
        acertou = True
    else:
        if y < x:
            print('Mais...Tente denovo')
        elif y > x:
            print('Menos...Tente denovo')
        else:
            print('Você acertou de primeira!')
if c != 1:
    print(f'Você acertou! Era {x}, mas você tentou {c} vezes')
