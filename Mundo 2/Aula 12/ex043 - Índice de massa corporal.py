h = float(input('Digite sua altura (m): '))
m = float(input('Digite seu peso (Kg): '))
imc = m / (h*2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < imc < 25:
    print('Parabéns, Você está no peso ideal.')
elif 25 < imc < 30:
    print('Você está com sobrepeso.')
elif 30 < imc < 40:
    print('Você está em obesidade.')
else:
    print('Você esta em obesidade mórbida, cuidado.')
