from random import randrange
from time import sleep

print('Analize de multa')
v = randrange(50, 120)
print(f'Esse carro estava a {v}')
print('Calculando...')
sleep(3)

print('Não multado' if v <= 80 else print(f'multado em R${(v-80)*7:.2f}'))
