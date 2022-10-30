from datetime import datetime
maior = 0
menor = 0

for c in range(1, 8):
    p = int(input('Em qual ano a {}º pessoa nasceu? '.format(c)))
    print('A {} pessoa tem {} anos!'.format(c, datetime.today().year - p))
    if datetime.today().year - p < 18:
        menor +=1
    else:
        maior +=1
print('Das sete pessoas analizadas,\n'
      ' {} pessoas atingiram a maioridade,\n'
      ' enquanto {} pessoas ainda sao menores.'.format(maior, menor))
