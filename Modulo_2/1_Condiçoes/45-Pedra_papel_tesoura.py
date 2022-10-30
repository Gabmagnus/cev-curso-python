import random
j = int(input('Escolha uma opção:\n'
              '[ 1 ] Pedra\n'
              '[ 2 ] Papel\n'
              '[ 3 ] Tesoura\n'
              '»» '))

jog = ['PEDRA', 'PAPEL', 'TESOURA']
pc = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(pc)

if j == 1:
    print('Você escolheu {},\n'
          'O Computador escolheu {}\n'.format(jog[j-1], pc[1-1]))
    if pc[1-1] == 'PAPEL':
        print('VOCÊ PERDEU!')
    elif pc[1-1] == 'TESOURA':
        print('VOCÊ VENCEU!')
elif j == 2:
    print('Você escolheu {},\n'
          'O Computador escolheu {}\n'.format(jog[j-1], pc[1-1]))
    if pc[1-1] == 'TESOURA':
        print('VOCÊ PERDEU!')
    elif pc[1-1] == 'PEDRA':
        print('VOCÊ VENCEU!')
elif j == 3:
    print('Você escolheu {},\n'
          'O Computador escolheu {}\n'.format(jog[j-1], pc[1-1]))
    if pc[1-1] == 'PEDRA':
        print('VOCÊ PERDEU!')
    elif pc[1-1] == 'PAPEL':
        print('VOCÊ VENCEU!')
if jog[j-1] == pc[1-1]:
    print('EMPATE')