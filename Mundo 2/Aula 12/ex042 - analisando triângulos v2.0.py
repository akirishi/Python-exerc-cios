print('Fazendo um triangulo')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segundo reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('É possível fazer um triângulo:')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Escaleno')
else:
    print('impossível vazer um triângulo')
