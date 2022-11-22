from libs import Moeda

p = float(input('Digite o preço: RS'))
print(f'A metade de {Moeda.real(p)} é {Moeda.metade(p, form=True)}')
print(f'O Dobro de {Moeda.real(p)} é {Moeda.dobro(p, form=True)}')
print(f'Aumentando 10% de {Moeda.real(p)}, temos {Moeda.aumento(p, 10, form=True)}')
# print(f'Diminuindo 13% de {Moeda.real(p)}, temos {Moeda.diminuir(p, 13, form=True)}')