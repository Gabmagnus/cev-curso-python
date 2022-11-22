n = int(input('Digite um numero: '))
cnt = 0

for c in range(1, n+1):
    if n % c == 0:
        cnt += 1
        print('\033[32m{}\033[m'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')

print('\nO Numero foi divisivel {} vezes'.format(cnt))
if cnt == 2:
    print('\033[32mE por isso ele É UM NUMERO PRIMO\033[m')
else:
    print('\033[31mE por isso ele NÃO É UM NUMERO PRIMO\033[m')