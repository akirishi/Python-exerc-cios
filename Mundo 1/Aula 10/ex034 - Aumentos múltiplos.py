print('Aumento!!')
x = float(input('Qual o seu salário?: '))
if x >= 1250:
    print(f'Seu novo salário é: {x*1.1:.2f}')
else:
    print(f'Seu novo salário é: {x*1.15:.2f}')
