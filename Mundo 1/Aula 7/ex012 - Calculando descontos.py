# Faça um programa que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

print('Desconto!!')
x = float(input('Valor do Produto:R$ '))
y = x - (x * 5 / 100)
print(f'Valor final:{y:.2f}')
