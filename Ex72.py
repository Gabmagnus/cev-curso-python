extenso = ('zero', 'um', 'Dois', 'Tres', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezeseis', 'dezesete', 'desenove', 'vinte')

n = int(input('Digite um numero de 0 a 20: »'))

while True:
    if n > 20 or n < 0:
        n = int(input('Numero invalido.\nDigite um numero de 0 a 20: »'))
    else:
        print(f'Você digitou o numero {n}, por extenso, {extenso[n]}')
        break