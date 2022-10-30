db = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(0, 3):
    for y in range(0, 3):
         db[x][y] = int(input(f'Digite um valor para entrar no [{x}] [{y}]: '))

for x in range(0, len(db)):
    for y in range(0, 3):
        print(f'[{db[x][y]:^5}]',end='')
    print()

