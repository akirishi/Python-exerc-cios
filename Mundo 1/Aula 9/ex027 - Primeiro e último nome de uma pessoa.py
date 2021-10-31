print('Primeiro e ultimo nome')
x = str(input('Digite seu nome completo: ').strip().lower().title())

print(f'Seu primeiro nome é {x.split()[0]}\n'
      f'Seu último nome é {x.split()[x.count(" ")]}')
