n = str(input('Digite seu nome completo: ')).strip()
nlist = n.split()

print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(nlist[0], nlist[len(nlist)-1]))