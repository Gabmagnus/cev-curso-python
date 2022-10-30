from random import randint
from time import sleep

qtdjogossorteados = int(input('Quantos jogos quer sortear?: '))
lista = []


for geradordelistasvazias in range(0, qtdjogossorteados):
    lista.append([])
    for geradordenumerosaleatorios in range(0, 6):
        lista[geradordelistasvazias].append(randint(1, 60))

for geradordelistasvazias in range(0, qtdjogossorteados):
    print(f'Jogo {geradordelistasvazias+1}: {lista[geradordelistasvazias]}')