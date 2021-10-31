# Escreva um programa que leia um valor em metros e
# o exiba convertendo em centímetros e milimitros.

print('Conversor de comprimento')
m = float(input('Valor em metros: '))
x = float(input('Digite\n'
                '1 para Km\n'
                '2 para Hm\n'
                '3 para Dam\n'
                '4 para dm\n'
                '5 para cm\n'
                '6 para mm\n'
                ''))
if x == 1:
    print(f'{m}m são {m / 1000}Km')
elif x == 2:
    print(f'{m}m são {m / 100}Hm')
elif x == 3:
    print(f'{m}m são {m / 10}Dam')
elif x == 4:
    print(f'{m}m são {m * 10}dm')
elif x == 5:
    print(f'{m}m são {m * 100}cm')
elif x == 6:
    print(f'{m}m são {m * 1000}mm')
