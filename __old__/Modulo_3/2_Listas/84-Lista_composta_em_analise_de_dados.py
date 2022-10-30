db = list()
maiores = list()
menores = list()
dado = list()
maior = 0
menor = float('inf')
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))

    if dado[1] == maior:
        maiores.append(dado[0])
    elif dado[1] > maior:
        maiores.clear()
        maior = dado[1]
        maiores.append(dado[0])

    if dado[1] == menor:
        menores.append(dado[0])
    elif dado[1] < menor:
        menores.clear()
        menor = dado[1]
        menores.append(dado[0])

    db.append(dado.copy())
    dado.clear()
    c = str(input('Deseja continuar? [S|N] ')).strip().upper()[0]
    if c != 'S':
        break
print(f'Você cadastrou {len(db)} pessoas')
print(f'O maior peso foi {maior}, peso de {maiores}')
print(f'O menor peso foi {menor}, peso de {menores}')
