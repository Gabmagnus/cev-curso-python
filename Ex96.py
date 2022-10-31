def area(x, y):
    print(f'A Area de {x} x {y} é de {x*y}m2')


print('*-' * 30)
print('Controle de terrenos')
print('*-' * 30)

area(float(input('Largura [m]: ')), float(input('Comprimento [m]: ')))