from lib import Moeda

p = float(input('Digite o preço: RS'))
print(f'A metade de {p} é {Moeda.metade(p)}')
print(f'O Dobro de {p} é {Moeda.dobro(p)}')
print(f'Aumentando 10% de {p}, temos {Moeda.aumento(p, 10)}')
print(f'Diminuindo 13% de {p}, temos {Moeda.diminuir(p, 13)}')