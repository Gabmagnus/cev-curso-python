def notas(*n, sit=False):
    sum = 0
    maior = 0
    menor = float('inf')
    db = {}
    db['Total'] = len(n)
    for c in range(0, len(n)):
        sum += n[c]
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
    db['maior'] = maior
    db['menor'] = menor
    db['media'] = sum / len(n)
    if sit == True:
        if db['media'] >= 7:
            db['situaçao'] = 'BOA'
        elif 7 > db['media'] >= 4:
            db['situaçao'] = 'RAZOAVEL'
        if 6 > db['media']:
            db['situaçao'] = 'RUIM'
    return(db)


print(notas(10, 4, 3, 6, sit=True))