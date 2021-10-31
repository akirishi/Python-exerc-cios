print('-' * 20)
print(f'{"KaBuM":^20}')
print('-' * 20)
nbarato = ''
c = barato = caro = total = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    c += 1
    if preco >= 1000:
        caro += 1
    if c == 1 or preco < barato:
        nbarato = nome
        barato = preco
    fim = str(input('Fim? [S/N]: ').strip().upper()[0])
    if 'S' in fim:
        break

print(f'O preço total a pagar é {total}')
if caro > 1:
    print(f'Há {caro} prdutos com valor acima de R$1000,00')
else:
    print(f'Há {caro} produto com valor acima de R$1000,00')
print(f'O produto mais barato é {nbarato}')
