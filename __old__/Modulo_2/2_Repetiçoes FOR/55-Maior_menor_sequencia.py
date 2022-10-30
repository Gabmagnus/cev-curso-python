maior = 0
menor = float("inf")

for c in range(1, 6):
    p = int(input('Qual o peso da {}º pessoa: '.format(c)))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
    print(maior)
    print(menor)
print('Das cinco pessoas analizadas,\n'
      ' O Menor peso é: {}.\n'
      ' O Maior peso é: {}.'.format(menor, maior))