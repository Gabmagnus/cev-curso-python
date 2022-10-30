import math
l1 = float(input('Cateto oposto: '))
l2 = float(input('Cateto adjacente: '))

hip = math.hypot(l1,l2)

print('A Hipotenusa entre {} e {} é igual a {:.2f}'.format(l1,l2,hip))
