lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print(f'O Valor {n} foi Adcionado!')
    else:
        print(f'O Valor {n} já existe, portanto NÃO foi adcionado!')
    c = str(input('Quer continuar?[ S | N ]: ')).strip().upper()[0]
    if c != 'S':
        break
print(sorted(lista))