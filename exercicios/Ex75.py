from gettext import find

tup = (int(input('Digite o primeiro valor » ')), int(input('Digite o Segundo valor » ')), int(input('Digite o Terceiro valor » ')), int(input('Digite o Quarto valor » ')))

print(f'O Valor 9 apareceu {tup.count(9)} vezes.')
print(f'O Valor 3 apareceu primeiro na {tup.index(3) + 1}º posiçao')
print('Os valores pares foram:', end=' ')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')
    else:
        pass
