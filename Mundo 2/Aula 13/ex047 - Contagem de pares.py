from time import sleep

for c in range(2, 51, 2):
    print(f'{c}', end=" ")
    sleep(0.2)
print(f'\n{"Acabou":=^20}')
