n = int(input('Digite um numero para ver seu fatorial: '))
c = n - 1

print('calculando fatorial de {}!: {} x '.format(n, n), end='')
while c != 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    n = n * (c)
    c -= 1
print(n)