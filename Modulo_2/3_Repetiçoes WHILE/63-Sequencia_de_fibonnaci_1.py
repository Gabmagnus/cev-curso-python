from time import sleep

t = int(input('Quantos termos você quer mostrar? '))
n1 = 1
n2 = 0
r = 0
c = 0

print('0', end=' » ')
while c != t-1:
    r = n1 + n2
    n1 = n2
    n2 = r
    c += 1
    print(r, end=' » ')
    sleep(0.3)
print('FIM!')
# 1, 1, 2, 3, 5, 8