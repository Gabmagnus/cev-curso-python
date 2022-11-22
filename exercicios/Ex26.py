f = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('A PRIMEIRA letra A aparece na {} posiçao'.format(f.find('A') + 1))
print('A ULTIMA letra A aparece na {} posiçao'.format(f.rfind('A') + 1))

