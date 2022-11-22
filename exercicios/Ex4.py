var = input('Digite Algo: ')

print('O Tipo primitivo desse valor é: {}'.format(type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('É um numero {}'.format(var.isnumeric()))
print('É Alfabético? {}'.format(var.isalpha()))
print('Está em Maiusculo? {}'.format(var.isupper()))
print('Está em minusculo? {}'.format(var.islower()))
print('Está Captalizada? {}'.format(var.istitle()))
