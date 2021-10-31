from datetime import date

print('Ano Bissexto')
x = int(input('Digite um ano (Digite 0 para o ano atual): '))

if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print(f'Sim, o ano de {x} é bissexto')
else:
    print(f'Não, o ano de {x} não é bissexto!\n'
          'Bom ano para você')
