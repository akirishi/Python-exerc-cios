# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjeacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

print('Calculo da Hipotenusa de um triângulo retânguo')

c1 = float(input('Digite o cateto oposto: '))
c2 = float(input('Digite o cateto adjacente: '))

print(f'O valor da hiponenusa é:{hypot(c1, c2):.2f}')
