from random import randint
rng = randint(0,5)
n = int(input('Escolha um numero!: '))

if rng == n:
    print('Voce venceu :)! o numero era {}'.format(rng))
else:
    print('Voce perdeu :(! o numero era {} e voce escolheu {}'.format(rng, n))