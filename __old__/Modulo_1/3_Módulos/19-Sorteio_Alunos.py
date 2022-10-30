import random

a1 = str(input('Aluno Um: '))
a2 = str(input('Aluno dois: '))
a3 = str(input('Aluno tres: '))
a4 = str(input('Aluno quatro: '))

n = str(random.choice([a1, a2, a3, a4]))

print('O Aluno sorteado foi {}'.format(n))

