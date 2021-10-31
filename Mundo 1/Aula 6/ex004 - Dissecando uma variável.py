# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele

print('informações')
x = input('Digite algo: ')
print(f'o tipo primitivo de {x} é:', type(x),
      f'{x} é um número?:', x.isnumeric(),
      f'{x} é uma letra ou palavra?:', x.isalpha(),
      f'{x}Só tem espaços?:', x.isspace(),
      f'{x}Esta em maiúsculas?:', x.isupper(),
      f'{x}Esta em minúscula?:', x.islower(),
      f'{x}Esta capitalizada?:', x.istitle())
