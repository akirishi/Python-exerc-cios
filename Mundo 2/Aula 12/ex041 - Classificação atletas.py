from datetime import date

print('faixa etária')
x = int(input('Digite o ano de nascimento: '))
y = date.today().year
z = y - x

if z <= 9:
    print(f'Esse é um atleta mirim de {z} anos')
elif 9 < z <= 14:
    print(f'Esse é um atleta infantil de {z} anos')
elif 14 < z <= 19:
    print(f'Esse é um atleta junior de {z} anos')
elif 19 < z <= 20:
    print(f'Esse é um atleta sênior de {z} anos')
else:
    print(f'Esse é um atleta master de {z} anos')
