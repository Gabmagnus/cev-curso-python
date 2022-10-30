n = int(input('Escolha um numero inteiro: '))
c = int(input(('Escolha uma das bases para conversão: \n'
      '[ 1 ] para BINÁRIO \n'
      '[ 2 ] para OCTAL \n'
      '[ 3 ] para HEXADECIMAL \n')))

if c == 1:
    print('{} convertido para binario é {}'.format(n, format(n, 'b')))
elif c == 2:
    print('{} convertido para octal é {}'.format(n, format(n, 'o')))
elif c == 3:
    print('{} convertido para hexadecimal é {}'.format(n, format(n, 'x')))
