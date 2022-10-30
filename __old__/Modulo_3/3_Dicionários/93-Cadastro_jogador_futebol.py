db = {

}
golstotal = 0
db['jogador'] = str(input('Nome do jogadoor: '))
np = (int(input('Numero de partidas: ')))
db['gols'] = []
for c in range(0, np):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    db['gols'].append(gol)
    golstotal += gol
db['total'] = golstotal

print('*-'*30)
print(db)
print('*-'*30)
for k, v in db.items():
    print(f'O Campo {k} tem o valor de {v}')
print('*-'*30)
print(f'O Jogador {db["jogador"]} jogou {len(db["gols"])}')
for c in range(0, len(db["gols"])):
    print(f'     »» Na partida {c+1}, {db["jogador"]} fez {db["gols"][c]}')
