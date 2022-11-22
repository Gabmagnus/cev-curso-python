n = float(input('Salario atual: '))
porc = (n/100)*15
print('Com um aumento de {:.2f}BRL, o novo salário é de {:.2f}BRL'.format(porc, n+porc))
