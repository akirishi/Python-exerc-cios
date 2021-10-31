palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDADR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print(f'\nNa palavara {p} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.lower(), end=' ')
