# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado.

print('Alugue de carro')

x = int(input('Quantos dias o carro foi alugado?: '))
y = float(input('Quantos Km rodados?: '))

print(f'O total a pagar é R${x * 60 + y * 0.15:.2f}')
