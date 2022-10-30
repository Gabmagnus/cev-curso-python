maior = 0
menor = 0

for c in range(1, 6):
    p = int(input('Qual o peso da {}º pessoa: '.format(c)))
    if p :
        menor = p
    else:
        maior +=1
print('Das cinco pessoas analizadas,\n'
      ' O Menor peso é: {}.\n'
      ' O Maior peso é: {}.'.format(maior, menor))
