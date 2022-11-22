sn = 'S'
c = 0
sum = 0
maior = 0
menor = float('inf')

na = int(input('Digite um numero: '))
while sn in 'Ss':
    sum += na
    c += 1
    if na > maior:
        maior = na
    if na < menor:
        menor = na
    sn = str(input('Quer continuar?[ S/N ]'))[0].strip().upper()
    if sn in 'Ss':
        na = int(input('Digite um numero: '))

print('Maior número digitado: {}\n'
      'Menor número digitado: {}\n'
      'Média dos numeros digitados: {}\n'.format(maior, menor, sum/c))