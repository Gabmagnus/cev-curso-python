import math
n = math.radians(float(input('Digite seu angulo: ')))

s = math.sin(n)
c = math.cos(n)
t = math.tan(n)

print('O Angulo de {:.2f}º tem como:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(n, s, c, t))

