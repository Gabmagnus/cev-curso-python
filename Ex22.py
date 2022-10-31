n = str(input('Escreva seu nome completo: ')).strip()
nwnspc = n.replace(' ', '')
nlist = n.split()

print('Nome captalizado: ' + n.upper())
print('Nome minusculo: ' + n.lower())
print('Numero de letras: {}'.format(len(nwnspc)))
print('Numero de letras do primeiro nome: {}'.format(len(nlist[0])))
