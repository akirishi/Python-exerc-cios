# Escreva um programa que leia um valor em metros e
# o exiba convertendo em centímetros e milimitros.

print('Conversor de comprimento')
m = float(input('Valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
x = float(input('Digite\n'
                '1 para Km\n'
                '2 para Hm\n'
                '3 para Dam\n'
                '4 para dm\n'
                '5 para cm\n'
                '6 para mm\n'
                ''))
if x == 1:
    print(f'{m}m são {km}Km')
if x == 2:
    print(f'{m}m são {hm}Hm')
if x == 3:
    print(f'{m}m são {dam}Dam')
if x == 4:
    print(f'{m}m são {dm}dm')
if x == 5:
    print(f'{m}m são {cm}cm')
if x == 6:
    print(f'{m}m são {mm}mm')
