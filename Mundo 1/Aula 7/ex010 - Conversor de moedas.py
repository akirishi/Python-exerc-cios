# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode
# comprar
from time import sleep
import requests  # Biblioteca para a api

req = requests.get('https://economia.awesomeapi.com.br/all/')  # API
cot = req.json()
print('Conversão de moeda')
val = int(input('Digite o valor a ser convertido: R$ '))  # input do usuário
x = int(input('1 - ($) Dólar Americano'  # menu
              '\n2 - (€) Euro'
              '\n3 - (£) Libra Esterlina'
              '\n4 - (¥) Iene Japonês'
              '\n5 - () Dólar Australiano'
              '\n>'))
print('=-' * 20)
print('Calculando...')
print('=-' * 20)
sleep(2)
# Conversão e apresentação ao usuário
if x == 1:
    print(f'A moeda {cot["USD"]["name"]}'
          f'\nÚltima cotação em {cot["USD"]["create_date"]}'
          f'\nEsta no valor de R$ {cot["USD"]["bid"]}'
          f'\nConvertendo R$ {val}, você teria U$ {val / float(cot["USD"]["bid"]):.2f}')
elif x == 2:
    print(f'Moeda {cot["EUR"]["name"]}'
          f'\nÚltima cotação em {cot["EUR"]["create_date"]}'
          f'\nEstá no valor de R$ {cot["EUR"]["bid"]}'
          f'\nConvertento R$ {val}, você teria € {val / float(cot["EUR"]["bid"]):.2f}')
elif x == 3:
    print(f'Moeda {cot["GBP"]["name"]}'
          f'\nÚltima cotação em {cot["GBP"]["create_date"]}'
          f'\nEstá no valor de R$ {cot["GBP"]["bid"]}'
          f'\nConvertento R$ {val}, você teria £ {val / float(cot["GBP"]["bid"]):.2f}')
elif x == 4:
    print(f'Moeda {cot["JPY"]["name"]}'
          f'\nÚltima cotação em {cot["JPY"]["create_date"]}'
          f'\nEstá no valor de R$ {cot["JPY"]["bid"]}'
          f'\nConvertento R$ {val}, você teria ¥ {val / float(cot["JPY"]["bid"]):.2f}')
elif x == 5:
    print(f'Moeda {cot["AUD"]["name"]}'
          f'\nÚltima cotação em {cot["AUD"]["create_date"]}'
          f'\nEstá no valor de R$ {cot["AUD"]["bid"]}'
          f'\nConvertento R$ {val}, você teria A$ {val / float(cot["AUD"]["bid"]):.2f}')
