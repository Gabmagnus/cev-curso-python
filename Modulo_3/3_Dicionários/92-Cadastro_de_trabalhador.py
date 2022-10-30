from datetime import datetime
db = {
    'nome': str(input('Nome: ')),
    'idade': (datetime.today().year - (int(input('Ano de nascimento: ')))),
    'cpts': int(input('Carteira de trabalho: [0 - Náo tem]: '))
}
if db['cpts'] != 0:
    db['ano_de_contrataçao'] = int(input('ano de contrataçao: '))
    db['salario_mensal'] = int(input('Salário mensal: '))
    db['aposentadoria'] = db['idade'] + (35 - (datetime.today().year - db['ano_de_contrataçao']))


print('*-'*30)
for k, v in db.items():
    if k == 'cpts' and v == 0:
        print(f'     » {k}: NÃO CADASTRADO!')
    else:
        print(f'     » {k}: {v}')