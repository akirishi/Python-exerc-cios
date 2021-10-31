# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode
# comprar

from time import sleep

print('Conversão de moeda')
brl = float(input('Qunatos reais você tem? R$: '))
dol = brl / 5.51
eur = brl / 6.57
lbr = brl / 7.62
ien = brl / 0.051
doa = brl / 0.24
x = int(input('Digite\n'
              '1 para ($) Dólar\n'
              '2 para (€) Euro\n'
              '3 para (£) Libra Esterlina\n'
              '4 para (¥) Iene\n'
              '5 para (A$) Dólar Australiano\n'
              ''))

print('=-' * 20)
print('Calculando...')
print('=-' * 20)
sleep(2)

if x == 1:
    print(f'R${brl:.2f} equivalem a ${dol:.2f}')
elif x == 2:
    print(f'R${brl:.2f} equivalem a €{eur:.2f}')
elif x == 3:
    print(f'R${brl:.2f} equivale a £{lbr:.2f}')
elif x == 4:
    print(f'R${brl:.2f} equivale a ¥{ien:.2f}')
elif x == 5:
    print(f'R${brl:.2f} equivale a A${doa:.2f}')
else:
    print(f'Opcão inválida, tente novamente')
