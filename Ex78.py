import random
nlist = list()
for c in range(0, 5):
    n = int(input(f'Digite um valor na posição {c}: '))
    nlist.append(n)

print(f'Os valores digitados foram: {nlist}')
print('\nO MAIOR valor digitado foi: {}, nas posiçoes: '.format(sorted(nlist)[(len(nlist)-1)]), end='')
for r in range(0, len(nlist)):
    if nlist[r] == sorted(nlist)[(len(nlist)-1)]:
        print(nlist.index(nlist[r], r), end='... ')
print('\nO MENOR valor digitado foi: {}, nas posiçoes: '.format(sorted(nlist)[0]), end='')
for r in range(0, len(nlist)):
    if nlist[r] == sorted(nlist)[0]:
        print(nlist.index(nlist[r], r), end='... ')