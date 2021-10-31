print(f'{"Tabuada":=^19}')
x = int(input('Número: '))

# print(f'{x} X {1:2} = {x * 1}'
#       f'{x} X {3:2} = {x * 3}'
#       f'{x} X {4:2} = {x * 4}'
#       f'{x} X {5:2} = {x * 5}'
#       f'{x} X {6:2} = {x * 6}'
#       f'{x} X {7:2} = {x * 7}'
#       f'{x} X {8:2} = {x * 8}'
#       f'{x} X {9:2} = {x * 9}'
#       f'{x} X {10:2} = {x * 10}')

for c in range(1, 11):
    print(f'{x} X {c:2} = {x * c}')
