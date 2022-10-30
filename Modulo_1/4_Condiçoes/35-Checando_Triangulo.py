n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))

m = [n1, n2, n3]
m.sort

if m[2] < m[0]+m[1]:
    print('PODE SER UM TRIANGULO')
else:
    print('NAO PODE SER UM TRIANGULO')

