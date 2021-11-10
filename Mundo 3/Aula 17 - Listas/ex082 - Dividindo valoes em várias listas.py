from random import randint

val = list()
par = list()
imp = list()

for c in range(0, randint(5, 10)):
    x = randint(0, 100)
    val.append(x)
    print(f'O valor {x} foi adicionado a lista')
for num in val:
    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        imp.append(num)

print(f'A lista completa é           {val}\n'
      f'A lista apenas com pares é   {par}\n'
      f'A lista paenas com impares é {imp}')
