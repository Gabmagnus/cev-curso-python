from random import randint
rng = randint(0,10)
t = int(input('=-'*15 + '\nESCOLHA UM NÚMERO\nDE 0 a 10\n' + '=-'*15 + '\n» '))
tryes = 1
while t != rng:
    tryes += 1
    t = int(input('=-' * 15 + '\nVocê errou!\nO numero era {}\nTente denovo!\n'.format(rng) + '=-' * 15 + '\n» '))
    rng = randint(0, 10)
print('=-' * 15 + '\nVocê Acertou!!!!\nO numero era {}\nVoce demorou {} tentatiivas!\n'.format(rng, tryes) + '=-' * 15)
