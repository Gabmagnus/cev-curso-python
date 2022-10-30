from random import randint

def sorteio(lista):
    print(f'Sorteando 5 valores aleatorios: ', end='')
    for c in range(0, 5):
        r = randint(1, 5)
        lista.append(r)
        print(f'{r}', end=' ')
    print()

def somapar(lista):
    sum = 0
    for s in range(0, len(lista)):
        if lista[s] % 2 == 0:
            sum += lista[s]
    print(f'somando os valores pares de {lista} temos {sum}')

numeros = []
sorteio(numeros)
somapar(numeros)