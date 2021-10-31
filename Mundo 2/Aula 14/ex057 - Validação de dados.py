s = ''
while s not in 'MF':
    s = str(input('Digite seu sexo:\n'
                  '[F] feminino\n'
                  '[M] masculino\n'
                  '').strip().upper()[0])
    if s != 'F' != 'M':
        print('Sexo inválido!')

print('Cadastro completo!')
