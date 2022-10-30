db = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacoluna = 0
maiorsegunda = 0
for x in range(0, 3):
    for y in range(0, 3):
        db[x][y] = int(input(f'Digite um valor para entrar no [{x}] [{y}]: '))
        if db[x][y] % 2 == 0:
            somapar += db[x][y]
        if x == 2:
            somacoluna += db[x][y]
        if x == 1 and db[x][y] > maiorsegunda:
            maiorsegunda = db[x][y]

print('*-'*30)
for x in range(0, len(db)):
    for y in range(0, 3):
        print(f'[{db[x][y]:^5}]',end='')
    print()

print('*-*'*30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores pares é {somacoluna}')
print(f'O maior valor da segunda coluna é {maiorsegunda}')


#somapar == 2+4+6+8=20
#soma3coluna= 7+8+9=24