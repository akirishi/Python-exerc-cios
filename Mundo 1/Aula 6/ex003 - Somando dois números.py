# Crie um programa que leia dois númeos e mostre a soma
# entre eles

print(f'{"Soma":=^20}')
y = int(input('Quantos números vão ser somados?: '))
s = 0
for n in range(0, y):
    x = float(input('Digite um número: '))
    s += x
print(f'A soma é igual a {s:.2f}')
