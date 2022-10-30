r = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        r += n
print('O Resultado da soma dos numeros pares foi: {}'.format(r))