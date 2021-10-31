print('Testando o seu nome')
nome = str(input('Digite seu nome completo: ').strip())
print(f'Seu nome todo em maiúsculo é {nome.upper()}\n'
      f'Seu nome todo em minúsculas é {nome.lower()}\n'
      f'Seu nome tem {len(nome) - nome.count(" ")} letras\n'
      f'Seu primeiro nome tem {len(nome.split()[0])} letras')
