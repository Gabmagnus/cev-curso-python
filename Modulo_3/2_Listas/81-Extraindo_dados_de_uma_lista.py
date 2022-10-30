lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c = str(input('Deseja continuar? [S|N]: ')).strip().upper()[0]
    if c != 'S':
        break
lista.sort(reverse=True)

print(f'-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente sao {lista}')
if 5 not in lista:
    print(f'O numero 5 nao esta na lista!.')
else:
    print('O numero 5 está na lista!')