# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do
# escolhido

from random import choice

print('Quem vai apagar o quadro?')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
x = [a1, a2, a3, a4]
print(f'O escolhido foi {choice(x)}')
