print('Fazendo um triangulo')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segundo reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 < r3:
    if (r1 + r2) > r3:
        print('É possível fazer um triângulo')
    else:
        print('É impossível fazer um triângulo')
elif r2 < r3 < r1:
    if (r2 + r3) > r1:
        print('É possível fazer um triângulo')
    else:
        print('É impossível fazer um triângulo')
elif r3 < r1 < r2:
    if (r3 + r1) > r2:
        print('É possível fazer um triângulo')
    else:
        print('É impossível fazer um triângulo')