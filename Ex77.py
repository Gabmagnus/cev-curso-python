list = ('APRENDER', 'PROGRAMAR',
        'LINGUAGEM', 'PYTHON',
        'CURSO', 'GRATIS',
        'ESTUDAR', 'PRATICAR',
        'TRABALHAR', 'MERCADO',
        'PROGRAMADOR', 'FUTURO')

vog = ''
for c in range(0, len(list)):
    vog = [each for each in list[c] if each in 'AEIOU']
    print('\nNa palavra {} temos '.format(list[c]),end='',)
    for d in range(0, len(vog)):
        print(vog[d], end=' ')
