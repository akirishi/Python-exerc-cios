c = s = 0
while True:
    x = float(input(f'Digite o {c + 1}º número: '))
    if x != 999:
        c += 1
        s += x
    else:
        break
print(f'A soma entre os {c} valores digitados é {s}')
