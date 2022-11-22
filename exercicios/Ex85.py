db = [list(), list()]

for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        db[0].append(n)
    else:
        db[1].append(n)
print(f'Os numeros pares são {db[0]}')
print(f'Os numeros impares são {db[1]}')