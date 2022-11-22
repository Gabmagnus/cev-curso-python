db = []
count = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota um: '))
    nota2 = float(input('Nota dois: '))
    med = (nota1 + nota2) / 2
    db.append([nome, nota1, nota2, med])
    c = str(input('Deseja continuar? [S|N] ')).strip().upper()[0]
    if c != 'S':
        break

print('-*'*30)
print(f'No.  Nome', ' '*13 , f' Media')
for c in range(0, len(db)):
    print(f'{c+1}', ' | ', f'{db[c][0]: <20}', f'{db[c][3]:>2.1f}')