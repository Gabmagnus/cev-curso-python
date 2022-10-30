n = float(input('Preço atual do produto: '))
ndesc = (n/100)*5
print('Com 5% de desconto({:.2f}BRL) o novo preço do produto fica {:.2f}BRL'.format(ndesc, n-ndesc))
