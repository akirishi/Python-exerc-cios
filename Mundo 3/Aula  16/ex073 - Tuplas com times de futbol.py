from time import sleep

time = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético-MG', 'Athlético-PR', 'Cruzeiro', 'Botafogo', 'Santos,',
        'Bahia', 'Fluminense', 'Corinthias', 'Chapecoense', 'Ceará', 'Vasco',
        'Sport', 'América-MG', 'Vitória', 'Paraná')
print('=-'*40)
print('Top 5 times: '
      f'{time[:5]}')
print('=-'*40)
sleep(1)
print('Últimos 4 times: '
      f'{time[-4:]}')
print('=-'*40)
sleep(1)
print('Times em ordem alfabética: '
      f'{sorted(time)}')
print('=-'*40)
sleep(1)
print(f'A Chapecoense está na {time.index("Chapecoense") + 1}ª posição')
print('=-'*40)
sleep(1)
