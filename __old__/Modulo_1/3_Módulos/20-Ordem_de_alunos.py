from random import shuffle

a1 = str(input('Aluno Um: '))
a2 = str(input('Aluno dois: '))
a3 = str(input('Aluno tres: '))
a4 = str(input('Aluno quatro: '))
l = [a1, a2, a3, a4]
shuffle(l)

print('O Aluno sorteado foi {}'.format(l))


