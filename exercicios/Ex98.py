from time import sleep


def contador(i, f, p):
    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
    print('*-' * 30)
    print(f'Chegando do valor {i} no valor {f} de {p} em {p}')
    print('*-' * 30)
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
        print('fim')
    else:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.3)
        print('fim')



contador(0,10,1)
contador(10, 0, 2)
print('Agora é sua vez!')
contador(int(input('Inicio: ')), int(input('Final: ')), int(input('Passo: ')))