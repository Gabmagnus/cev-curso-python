plus18 = 0
sub20 = 0
hom = 0
cnt= 0

while True:
    n = str(input('Nome: '))
    a = int(input('Idade: '))
    s = str(input('Sexo[ M / F ]: '))[0].strip().upper()

    if a >= 18:
        plus18 += 1
    if a < 20 and s == 'F':
        sub20 += 1
    if s == 'M':
        hom += 1
    cnt += 1
    c = str(input('Deseja continuar?[ S / N ]: '))[0].strip().upper()
    if c != 'S':
        print('\n\nPrograma encerrado! Foram cadastradas {} pessoas\n'
              'Foram cadastrados {} homens,\n'
              'Foram cadastradas {} pessoas com mais de 18,\n'
              'foram cadastradas {} mulheres com menos de 20.'.format(
            cnt, hom, plus18, sub20
        ))
        break


