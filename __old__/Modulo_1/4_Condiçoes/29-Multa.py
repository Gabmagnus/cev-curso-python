v = int(input('Digite a velocidade do carro: '))

if v > 80:
    print('Multado! Você execeu o limite de velocidade permitido que é 80Km/h'
          '\nDeve pagar uma multa de {},00BRL!'.format((v-80)*7))
print('tenha um bom dia, diriga com segurança!')
