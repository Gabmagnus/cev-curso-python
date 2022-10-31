n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))
n3 = float(input('Nota tres: '))


m = (n1+n2+n3)/3

if m < 5:
    r = 'REPROVADO'
elif m > 7:
    r = 'APROVADO'
else:
    r = 'RECUPERAÇAO'

print('Com uma media de {:.2F} voce foi {}'.format(m, str(r)))
n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))
n3 = float(input('Nota tres: '))


m = (n1+n2+n3)/3

if m < 5:
    r = 'REPROVADO'
elif m > 7:
    r = 'APROVADO'
else:
    r = 'RECUPERAÇAO'

print('Com uma media de {:.2F} voce foi {}'.format(m, str(r)))
