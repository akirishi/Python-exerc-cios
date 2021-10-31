print('Sua cidade é santa?')

cidade = str(input('Digite sua cidade: ').strip().lower())

if cidade[:5] == 'santo':
    print('Sim, sua cidade comeca com Santo')
else:
    print('Não, sua cidade não começa com Santo')
