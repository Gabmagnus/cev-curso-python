def ficha(j='<Desconhecido>', g=0):
    return(f'O Jogador {j} fez {g} gols no campeonato')


j = (input('Nome do jogador: '))
n = (input('Numero de gols: '))

if n.isnumeric():
    n = int(n)
else:
    n = 0

if j.strip() == '':
    print(ficha(g=n))
else:
    print(ficha(j, n))
