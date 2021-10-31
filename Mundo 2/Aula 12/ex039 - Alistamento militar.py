from datetime import date

x = int(input('Digite seu ano de nascimento: '))
y = date.today().year

if (y - x) < 18:
    print(f'Você precisará se alistar em {18 - (y - x)} anos')
elif (y - x) == 18:
    print('Você precisa se alistar esse ano')
else:
    print(f'Você esta atrasado {(y - x) - 18} anos para o alistamento')
