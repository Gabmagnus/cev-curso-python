print('='*10)
print('10 PRIMEIROS TERMOS DE UMA PA'.title())
print('='*10)

qtd = 10
pt = int(input('Primeiro Termo: '))
ptinit = pt
r = int(input('Razão: '))
dc = pt + (qtd-1) * r


while True:
    if pt < dc:
        print(pt, end=' » ')
        pt += r
    else:
        qtd += int(input('\nDeseja continuar? se sim indique o numero de casas, se nao, digite 0: '))
        dc = ptinit + (qtd-1) * r
        if qtd == 10:
            break
print('Acabou!')