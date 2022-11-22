db = {}

db['nome'] = str(input('Nome: '))
db['media'] = float(input(f'Média de {db["media"]}: '))
if db['media'] >= 7:
    db['resultado'] = 'APROVADO!'
else:
    db['resultado'] = 'REPROVADO!'


print(f'Nome: {db["nome"]}\n'
      f'Média: {db["media"]}\n'
      f'A situaçao de {db["nome"]} é {db["resultado"]}')