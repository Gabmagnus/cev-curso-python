from time import sleep


def maior(*num):
    maiornum = 0
    print('Analisando valores passados: ')
    sleep(0.6)
    print(f'{num} foram informados {len(num)} ao todo!')
    for c in range(0, len(num)):
        if num[c] > maiornum:
            maiornum = num[c]
    print(f'O Maior numero é igual a {maiornum}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 0, 7)
maior(1, 2)
maior(6)
maior()