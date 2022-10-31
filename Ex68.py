import random
parouimpar = ['PAR', 'IMPAR']
res = ''
wstrk = 0
while True:
    rng = random.randint(0, 10)
    jog = int(input('Escolha um numero: '))
    poi = str(input('Par ou impar? [P/I]'))[0].strip().upper()

    if poi not in 'PI':
        print('Opçao invalida, jogo acabou!')
        break
    if (rng+jog) % 2 == 0:
        res = parouimpar[0]
    else:
        res = parouimpar[1]

    if poi == res[0]:
        wstrk += 1
        print('-='*30 +
              '\nO Computador pensou no numero {}\n'
              'você no numero {}\n'
              'o resultado foi de {}, numero {}\n'
              'Você VENCEU! Conseguiu uma winstreak de [{}]\n'.format(rng,jog,rng+jog,res,wstrk)
              + '-='*30)
    else:
        print('-='*30 +
              '\nO Computador pensou no numero {}\n'
              'você no numero {}\n'
              'o resultado foi de {}, numero {}\n'
              'Você PERDEU! Conseguiu uma winstreak de [{}]\n'.format(rng,jog,rng+jog,res,wstrk)
              + '-='*30)
        wstrk = 0