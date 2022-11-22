from re import S


while True:
    n = str(input('Funçao ou biblioteca » '))
    print('\033[1;32;40m*-'*30, '')
    print('\033[m\033[1;32;40m', f'Mostrando a funçao: {n}'.center(59))
    print('\033[m\033[1;32;40m*-'*30)
    print('\033[1;31;40m*')
    help(n)
    print('\033[m')