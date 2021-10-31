from datetime import date
from time import sleep

y = date.today().year
print(f'Contagem regressiva para o fim do ano de {y}')

for c in range(10, -1, -1):
    print(f'{c}')
    sleep(1)

print(f'{"Faliz Ano Novo":!^35}')
