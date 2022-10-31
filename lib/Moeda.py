def metade(n, form=False):
    if form:
        return f'RS{n/2}'
    else:
        return n/2


def dobro(n, form=False):
    if form:
        return f'RS{n*2}'
    else:
        return n*2


def aumento(n, p, form=False):
    m = n * p / 100
    if form:
        return f'RS{n + m}'
    else:
        return m + n


def diminuir(n, p, form=False):
    m = n * p / 100
    if form:
        return f'RS{n - m}'
    else:
        return n - m


def real(n):
    return f'RS{n:.2f}'


def resumo(n, a, d):
    print('-'*30)
    print('RESUMO DE VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:{real(n): >15}')
    print(f'Dobro do preço:{real(dobro(n)): >17}')
    print(f'Metade do preço:{real(metade(n)): >15}')
    print(f'{a}% de aumento:{real(aumento(n, a)): >16}')
    print(f'{d}% de redução:{real(diminuir(n, d)): >16}')


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def leiadinheiro(n):
    valido = False
    while not valido:
        m = str(input(n)).replace(',', '.').strip()
        if m.isalpha() or m == '':
            print(f'"{m}" é um valor inválido, tente outro!')
        else:
            return float(m)
            valido = True
