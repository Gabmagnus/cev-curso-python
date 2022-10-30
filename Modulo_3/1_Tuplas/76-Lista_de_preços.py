list = ('Lápis', 1.75,
        'Borracha', 2.00,
        'Caderno', 15.90,
        'Estojo', 25.00,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'livros', 34.90)

print(f'{"-"*30}')
print(f'{"LISTAGEM DE PREÇOS":^30}')
print(f'{"-"*30}')
for c in range(0, len(list), 2):
    print(f'{list[c]:.<20}', f'RS{list[c+1]:>6.2f}')
print(f'{"-"*30}')