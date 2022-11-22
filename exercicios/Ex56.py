hmv = ['', 0]
agemed = 0
fcount = 0
fagedcount = 0
for c in range(1, 5):
    print('»»»»»» {}º PESSOA «««««««'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()

    agemed += idade
    if sexo == 'M':
        if idade > hmv[1]:
            hmv = [nome, idade]
    if sexo == 'F':
        if idade < 20:
            fagedcount += 1

print('A média deidade do grupo é de {} anos.'.format(agemed/4))
print('O homem mais velho de {} anos e se chama {}.'.format(hmv[1], hmv[0]))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(fagedcount))




#4 pessoas
#nome idade sexo
#homem mais velho
#mulheres menores de 20
#2017