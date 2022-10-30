n = int(input('Qual a distancia da viagem em KM? '))

if n <= 200:
    print('A viagem inteira custará {:.2f}BRL custando 50 centavos por km'.format(float(n)*0.50))
else:
    print('A viagem inteira custará {:.2f}BRL custando 45 centavos por km'.format(float(n)*0.45))


