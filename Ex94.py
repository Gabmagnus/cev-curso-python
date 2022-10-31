dados = {}
db = []
im = 0
pplcount = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M|F] ')).strip().upper()[0]
    while True:
        if dados['sexo'] not in 'MF':
            print(f'Sexo invalido!!, Tente novamente')
            dados['sexo'] = str(input('Sexo [M|F] ')).strip().upper()[0]
        else:
            break
    idade = int(input('Idade: '))
    dados['idade'] = idade
    im += idade
    db.append(dados.copy())
    pplcount += 1
    while True:
        k = str(input('Deseja continuar? [S|N]')).strip().upper()[0]
        if k not in 'SN':
            print('Valor incorreto: Digite SIM OU NÃO!')
        else:
            break
    if k == 'N':
        break

print('*-'*30)
print(f'A) Ao todo temos {len(db)} pessoas cadastradas.')
print(f'B) A Média de idade de todos os cadastrados é {im/pplcount} Anos')
print(f'As mulheres cadastradas foram: ', end='')
for c in range(0, len(db)):
    if db[c]['sexo'] == 'F':
        print(db[c]["nome"], end=' ')
print(f'\nLista de pessoas a cima da media de idade: ')
for c in range(0, len(db)):
    if db[c]['idade'] > im/pplcount:
        print(' »» ', str(db[c]).replace('{', '').replace('}', ''))

#db[0]['idade']
