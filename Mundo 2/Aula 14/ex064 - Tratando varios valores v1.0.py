from time import sleep

x = x1 = c = 0

print('Digite números\n'
      'Digite [999] para parar')
while x != 999:
    x = int(input('Digite um número: '))
    if x != 999:
        x1 += x
        c += 1
print(f'{c} foram digitados e asoma entre eles é {x1}\n'
      'Finalizando...')
sleep(1)
