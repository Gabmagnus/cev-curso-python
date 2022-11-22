na = 0
nsum = 0
t = 0

na = int(input('Digite um numero[ 999 para parar ]:'))
while na != 999:
    nsum += na
    t += 1
    na = int(input('Digite um numero!'))
print('Foram digitados {} numeros e a soma entre eles é de {}.'.format(t, nsum))
