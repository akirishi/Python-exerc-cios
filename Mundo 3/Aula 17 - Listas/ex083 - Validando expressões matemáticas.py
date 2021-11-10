
ex = str(input('Digite uma expressão: '))

open_par = close_par = 0
for letra in range(0, len(ex)):
    if ex[letra] == '(':
        open_par += 1
    elif ex[letra] == ')':
        close_par += 1

print(ex)
if open_par == close_par:
    print('Essa expressão é válida')
else:
    print('Essa expressão não é válida')
