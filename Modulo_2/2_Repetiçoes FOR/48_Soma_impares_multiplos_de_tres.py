cnt = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cnt += 1

print('A soma de {} valores soliciatdos é {}'.format(cnt, s))
