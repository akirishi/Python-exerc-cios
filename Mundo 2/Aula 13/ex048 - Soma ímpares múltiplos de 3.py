x = 0
y = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        x += c
        y += 1
print(f'A soma de {y} valores solicitados é {x}')
