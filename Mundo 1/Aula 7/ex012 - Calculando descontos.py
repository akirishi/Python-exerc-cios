# Faça um programa que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

print('Desconto!!')
x = float(input('Valor do Produto:R$ '))
print(f'Valor final:{x - (x * 5 / 100):.2f}')
