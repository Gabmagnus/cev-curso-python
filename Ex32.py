from datetime import datetime


n = int(input('Digite um ano: '))
if n == 0:
    n = datetime.today().year

if n%4 == 0 and n%100 != 0 or n%400 == 0:
    print('o ano de {} É um ano bissexto'.format(n))
else:
    print('o ano de {} Não é um ano bissexto'.format(n))