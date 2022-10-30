n = int(input('Digite um numero para ver sua tabuada: '))
for t in range(1, 11):
    print('{} x {} = {}'.format(n, t, n*t))