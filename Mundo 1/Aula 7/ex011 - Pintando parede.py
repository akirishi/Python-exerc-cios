# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade de
# tinta nescessária para pintá-la, sabendo que cada litro de
# tinta pinta uma área de 2 metros quadrados

print('Pintando sua parede!')
x = float(input('Altura da parede: '))
y = float(input('Largura da parede: '))
print(f'Para pintar a parede de {x * y}m² sera necessário {(x * y) / 2}L de tinta')
