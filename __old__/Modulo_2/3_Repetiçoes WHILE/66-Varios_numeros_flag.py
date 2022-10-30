na = 0
nsum = 0
t = 0

while True:
    na = int(input('Digite um numero[ 999 para parar ]:'))
    if na == 999:
        break
    nsum += na
    t += 1
print('Foram digitados {} numeros e a soma entre eles é de {}.'.format(t, nsum))
