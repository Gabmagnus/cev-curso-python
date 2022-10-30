p = float(input('Digite Seu Peso(Kg): '))#peso
h = float(input('Digite Sua Altura(m): '))#altura

imc = p/(h**2)
n = 'MUITO acima'

if imc < 18.5:
    n = 'ABAIXO'
elif imc >= 18.5 and imc < 25:
    n = 'EXATAMENTE na medida'
elif imc >= 25 and imc < 30:
    n = 'ACIMA'

print('Seu IMC é de {:.1f}\nVocê está {} do peso'.format(imc, n))
