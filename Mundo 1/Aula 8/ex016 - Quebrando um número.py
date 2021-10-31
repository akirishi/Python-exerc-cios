# Crie um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção inteira.

from math import trunc, sqrt
from random import randrange

x = float(sqrt(randrange(1, 1000)))
print(f'A porção inteira de {x} é {trunc(x)}')
