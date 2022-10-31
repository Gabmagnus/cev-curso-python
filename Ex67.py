while True:
    c = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while c != 11:
        print('{} x {} = {}'.format(n, c, n*c))
        c += 1
print('Finalizando programa!')