def leiaint(j):
    while True:
        k = input(j)
        if k.isnumeric():
            return int(k)
            break
        else:
            print('ERRO! Digite um valor válido!')


n = leiaint('Digite um numero: ')
print(f'Você acaba de digitar o numero {n}')
