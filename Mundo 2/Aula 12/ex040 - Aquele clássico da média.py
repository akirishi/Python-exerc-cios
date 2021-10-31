print('Média do aluno')
n = str(input('Digite o nome do aluno: ')).strip().lower().title()
print('Digite as notas:')

y = 0

for c in range(0, 3):
    x = float(input(f'Nota {c + 1}: '))
    y += x

m = y / 3

if m < 5:
    print(f'O aluno {n} foi reprovado com média {m:.2f}')
elif m < 6.9:
    print(f'O aluno {n} ficou de recuperação com média {m:.2f}')
else:
    print(f'O aluno {n} foi aprovado com média {m:.2f}')
