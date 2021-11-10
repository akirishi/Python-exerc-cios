from random import randint


num = list()


for c in range(0, 5):
    x = randint(0, 10)
    if c == 0:
        print(x)
        num.append(x)
        print('primeiro valor adicionado')
    elif c == 1:
        print(x)
        if x <= num[0]:
            num.insert(0, x)
            print('Vaolor adicionado na primeira posição')
        if x >= num[-1]:
            num.append(x)
            print('Vaolor adicionado na última posição')
    elif c == 2:
        print(x)
        if x <= num[0]:
            num.insert(0, x)
            print('Vaolor adicionado na primeira posição')
        if num[0] < x <= num[1]:
            num.insert(1, x)
            print('Valor adicionado na posição 1')
        if x >= num[-1]:
            num.append(x)
            print('Vaolor adicionado na última posição')
    elif c == 3:
        print(x)
        if x <= num[0]:
            num.insert(0, x)
            print('Vaolor adicionado na primeira posição')
        if num[0] < x <= num[1]:
            num.insert(1, x)
            print('Valor adicionado na posição 1')
        if num[1] < x <= num[2]:
            num.insert(2, x)
            print('Valor adicionado na posição 2')
        if x >= num[-1]:
            num.append(x)
            print('Vaolor adicionado na última posição')
    elif c == 4:
        print(x)
        if x <= num[0]:
            num.insert(0, x)
            print('Vaolor adicionado na primeira posição')
        if num[0] < x <= num[1]:
            num.insert(1, x)
            print('Valor adicionado na posição 1')
        if num[1] < x <= num[2]:
            num.insert(2, x)
            print('Valor adicionado na posição 2')
        if num[2] < x <= num[3]:
            num.insert(3, x)
            print('Valor adicionado na posição 3')
        if x >= num[-1]:
            num.append(x)
            print('Vaolor adicionado na última posição')

print(num)
