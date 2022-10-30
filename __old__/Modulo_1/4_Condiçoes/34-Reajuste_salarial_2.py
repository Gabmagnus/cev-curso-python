n = float(input('Salario atual: '))

if n > 1250:
    porc = (n/100)*10
else:
    porc = (n/100)*15

print('Com um aumento de {:.2f}BRL, o novo salário é de {:.2f}BRL'.format(porc, n+porc))
