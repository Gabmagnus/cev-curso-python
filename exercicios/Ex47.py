from time import sleep

for c in range(2, 51, 2):
    if c % 2 == 0:
        print(c, end='._.')
        sleep(0.2)