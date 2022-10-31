from time import sleep

jogador = {}
db = []
cod = 0
while True:
    jogador.clear()
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['gols'] = int(input(f'Quantas partidas {jogador["nome"]} Jogou? '))
    jogador['score'] = []
    for c in range(0, jogador['gols']):
        jogador['score'].append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = jogador['score'].copy()
    del jogador['score']
    jogador['total'] = len(jogador['gols'])
    db.append(jogador.copy())
    cod += 1
    while True:
        q = str(input('Deseja continuar [S|N]?')).strip().upper()[0]
        if q not in 'SN':
            print('Valor invalido!')
        else:
            break
    if q == 'N':
        break


print('*-'*30)
for k in jogador.keys():
    print(f'{k:<15}', end='')
    sleep(0.2)
print()
print('-'*30)
for k, v in enumerate(db):
    for d in v.values():
        print(f'{str(d):<15}', end='')
        sleep(0.2)
    print()
print()
print(db)
while True:
    dad = int(input('Quer mostrar os dados de qual jogador? [999 para sair]: '))
    if dad == 999:
        break
    else:
        print(f' »» levantamento do jogador {db[dad]["nome"]}')
        for v in range(0, len(db[dad]['gols'])):
            print(f'  »  No jogo {v+1}, {db[dad]["nome"]} fez {db[dad]["gols"]}.')
            sleep(0.2)