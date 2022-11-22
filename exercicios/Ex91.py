from random import randint
from time import sleep
from operator import itemgetter
db = {
    '1': randint(1, 6),
    '2': randint(1, 6),
    '3': randint(1, 6),
    '4': randint(1, 6)
}

ranking = sorted(db.items(), key=itemgetter(1), reverse=True)

print('*-'*30)
for p, j in db.items():
    print(f'O Jogador {p} tirou {j} no dado.')
    sleep(0.4)
print('--'*30)
print('\n» Ranking dos jogadores: «\n')
for c in range(0, len(ranking)):
    print(f'{c+1}º Lugar: Jogador {ranking[c][0]} com {ranking[c][1]}')
    sleep((0.4))





print(db)
print(ranking)
#for j in range(0, len(db)):
 #   print(f'{j}º Lugar: O Jogador {ranking[j]["jogador"]} com {ranking[j]["jogada"]}')