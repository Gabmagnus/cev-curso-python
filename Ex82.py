lista = list()
listap = list()
listaimp = list()
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        listap.append(n)
    else:
        listaimp.append(n)
    lista.append(n)
    c = str(input('Deseja continuar? [S|N]: ')).strip().upper()[0]
    if c != 'S':
        break

print(f'A lista completa é {lista}')
print(f'A Lista de PARES é {listap}')
print(f'A Lista de IMPARES é {listaimp}')