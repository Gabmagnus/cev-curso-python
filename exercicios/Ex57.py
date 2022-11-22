s = str(input('Digite seu sexo[M/F]: ')).upper().strip()[0]
while s not in 'MmFf':
    print('Opção errada, tente novamente!')
    s = str(input('Digite seu sexo[M/F]: ')).upper()
print('sexo {} registrado com sucesso'.format(s))