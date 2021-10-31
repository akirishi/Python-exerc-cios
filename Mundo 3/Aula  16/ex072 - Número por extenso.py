from time import sleep

núm = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito',
       'Desenove', 'Vinte')

print('-'*40)
print(f'{"Números por extenso":^40}')
print('-'*40)
while True:
    x = int(input('Digite um número entre 0 e 20: '))
    if 0 <= x <= 20:
        print(f'Você digitou o número {núm[x]}')
        y = str(input('Continuar? [S/N]: ').strip().upper())
        if y == 'N':
            break
    else:
        print('Tente novamente. ', end='')
print('Finalizando...')
sleep(1)
print('-'*40)
