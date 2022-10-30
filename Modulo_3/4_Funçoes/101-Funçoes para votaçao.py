from datetime import datetime

def voto(a):
    '''
    -> Define o voto de uma pessoa, a partir do ano de nascimento.
    :param a: ano de nascimento
    :return: com {i} anos o voto é {NEGADO/OPCIONAL/OBRIGATÓRIO}
    '''
    i = datetime.today().year - a
    if i < 16:
        return f'com {i} anos o voto é NEGADO'
    elif 16 <= i < 18 or 65 <= i:
        return f'com {i} anos o voto é OPCIONAL'
    elif 18 <= i < 65:
        return f'com {i} anos o voto é OBRIGATÓRIO'

print('~~' * 30)
print(voto(int(input('Seu ano de nascimento: '))))