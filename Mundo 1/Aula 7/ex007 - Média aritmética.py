# Desenvolva um programa que leia as notas de um aluno,
# calcule e mostre sua média

print('calculo da média do aluno')
nome = str(input('Digite o nome do aluno: '))
M = 0
# c = 1 para contabilizar as notas
c = 1
while not c == 4:
    n = float(input(f'{c}ª Nota: '))
    M += n
    c += 1
print(f'Média Final: {M / 3:.1f}')
print(f'Aluno {nome}, ' 'REPROVADO' if (M / 3) < 6 else f'Aluno {nome} APROVADO, PARABÉNS!')
