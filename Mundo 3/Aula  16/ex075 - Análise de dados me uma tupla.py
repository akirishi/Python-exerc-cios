from time import sleep

v = (int(input('Digite o 1º valor: ')),
     int(input('Digite o 2º valor: ')),
     int(input('Digite o 3º valor: ')),
     int(input('Digite o 4º valor: ')))
v9 = c = 0

print('=-'*20)
print('Analizando...')
print('=-'*20)
sleep(1)

print(f'Você digitou os valores: {v}')
if 9 in v:
    print(f'O valor 9 aparece {v.count(9)} vezes')
else:
    print('Não foi digitado nenhum valor 9')
if 3 in v:
    print(f'O valor 3 apareceu na {v.index(3)+1}ª posição')
else:
    print('Não foi digitado nenhum valor 3')
for n in v:
    if n % 2 == 0:
        c += 1
        print(n, end=' ')
if c == 0:
    print('Nenhum valor par foi digitado')
elif c == 1:
    print('foi o valor par digitado')
elif c > 1:
    print('foram os valores pares digitado')
