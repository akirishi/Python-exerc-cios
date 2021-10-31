# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo.

from random import randrange
from time import sleep
from math import sin, cos, tan, radians

print('Seno, cosseno e tangente')
x = float(input('Digite o Ângulo: '))

print(f'Analizando o ângulo {x}...')
sleep(randrange(1, 3))

print(f'O seno é {sin(radians(x)):.2f}\n'
      f'O cosseno é {cos(radians(x)):.2f}\n'
      f'E a tangente é {tan(radians(x)):.2f}')
