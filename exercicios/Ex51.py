print('='*10)
print('10 PRIMEIROS TERMOS DE UMA PA'.title())
print('='*10)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
dc = pt + (10-1) * r
for c in range(pt, dc, r):
    print(c, end=' » ')
print('Acabou!')