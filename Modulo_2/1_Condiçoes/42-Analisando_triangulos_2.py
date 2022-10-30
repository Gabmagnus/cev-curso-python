n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))

m = [n1, n2, n3]
m.sort()

if n1 == n2 and n1 == n3:
    t = 'EQUILATERO'
elif n1 == n2 or n1 == n3 or n2 == n3 or n2 == n1:
    t = 'ISOCELES'
elif n1 != n2 != n3:
    t = 'ESCALENO'

if m[2] < m[0]+m[1]:
    print('PODE SER UM TRIANGULO {}'.format(t))
else:
    print('NAO PODE SER UM TRIANGULO')

