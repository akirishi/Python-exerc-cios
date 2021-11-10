print('-' * 20)
print('Conversor de temperatura')
print('-' * 20)

while True:
    while True:
        escala = str(input('Qual a escala de tempertura inicial?\n'
                           '[C] - Celsius\n'
                           '[F] - Fahrenheit\n'
                           '[K] - Kelvin\n'
                           '>').strip().upper())
        if escala == 'C':
            Opt = str(input('Converter Celsius para:\n'
                            '[F] - para (ºF) Fahrenheit\n'
                            '[K] - para (K) Kelvin\n'
                            '>').strip().upper())
            break
        elif escala == 'F':
            Opt = str(input('Converter Fahrenheit para:\n'
                            '[C] - para (ºC) Celsius\n'
                            '[K] - para (K) Kelvin\n'
                            '>').strip().upper())
            break
        elif escala == 'K':
            Opt = str(input('Converter Kelvin para:\n'
                            '[F] - para (ºF) Fahrenheit\n'
                            '[C] - para (C) Celsius\n'
                            '>').strip().upper())
            break
        else:
            print('Opção inválida, tente novamente')

    if escala == 'C':
        C = float(input('Digite a temperatura em Celsius: '))
        if Opt == 'F':
            F = (C * 9 / 5) + 32
            print(f'{C:.2f} ºC é {F:.2f} ºF')
        elif Opt == 'K':
            K = C + 273.15
            print(f'{C:.2f} ºC é {K:.2f} K')
    elif escala == 'F':
        F = float(input('Digite a temperatura em Fahrenheits: '))
        if Opt == 'C':
            C = (F - 32) * 5 / 9
            print(f'{F:.2f} ºF é {C:.2f} ºC')
        elif Opt == 'K':
            K = (F - 32) * 5 / 9 + 273.15
            print(f'{F:.2f} ºF é {K:.2f} K')
    elif escala == 'K':
        K = float(input('Digite a temperatura em Kelvin: '))
        if Opt == 'C':
            C = K - 273.15
            print(f'{K:.2f} K é {C:.2f} ºC')
        elif Opt == 'F':
            F = (K - 273.15) * 9 / 5 + 32
            print(f'{K:.2f} K é {F:.2f} ºF')
    else:
        print('Opção inválida, tente novamente')
    terminou = str(input('Terminou? [S/N] ').strip().upper()[0])
    if terminou == 'S':
        break
print('Fim')
print('-' * 20)
