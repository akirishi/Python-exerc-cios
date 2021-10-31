# Crie em algoritmo que leia um número e mostre seu dobro,
# triplo e raiz quadrada

from math import (sqrt)

print('Dobro, Triplo e Raiz')
x = float(input('Número: '))
x2 = x * 2
x3 = x * 3
xr = sqrt(x)
print(f'O dobro de {x:.2f} é {x2:.2f}'
      f'O triplo é {x3:.2f} '
      f'E a raíz quadrada é {xr:.2f}')
