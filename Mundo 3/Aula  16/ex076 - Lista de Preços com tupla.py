listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
            'Tranferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas',
            22.3, 'Livro', 34.9)

c = 0
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
while True:
    print(f'{listagem[c]:.<30}R${listagem[c + 1]:>6.2f}')
    c += 2
    if c == len(listagem):
        break
print('='*40)
