n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

while True:
    n = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n» '))
    if n == 1:
        print('{} + {} = {}\n'.format(n1, n2, (n1 + n2)))
    elif n == 2:
        print('{} x {} = {}\n'.format(n1, n2, n1 * n2))
    elif n == 3:
        if n1 > n2:
            print('entre {} e {} o maior numero é {}\n'.format(n1,n2,n1))
        elif n1 < n2:
            print('entre {} e {} o maior numero é {}\n'.format(n1, n2, n2))
        else:
            print('Os números sao iguais!\n')
    elif n == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    else:
        break
