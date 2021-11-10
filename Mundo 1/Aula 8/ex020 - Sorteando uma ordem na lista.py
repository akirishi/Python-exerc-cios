# O mesmo professor do desafio 19 quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

print('Ordem de apresentação')
x = int(input('Qantos alunos vão apresentar? '))
alunos = list()
while len(alunos) < x:
    y = str(input(f'Aluno {len(alunos) + 1}: '))
    if y in alunos:
        print('Não pode haver alunos repetidos')
    else:
        alunos.append(y)
shuffle(alunos)
print(f'A ordem é {alunos}')
