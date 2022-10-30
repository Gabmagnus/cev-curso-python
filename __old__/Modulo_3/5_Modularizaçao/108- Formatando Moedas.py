from Uteis import Moeda

p = float(input('Digite o preço: RS'))
print(f'A metade de {Moeda.real(p)} é {Moeda.real(Moeda.metade(p))}')
print(f'O Dobro de {Moeda.real(p)} é {Moeda.real(Moeda.dobro(p))}')
print(f'Aumentando 10% de {Moeda.real(p)}, temos {Moeda.real(Moeda.aumento(p, 10))}')
print(f'Diminuindo 13% de {Moeda.real(p)}, temos {Moeda.real(Moeda.diminuir(p, 13))}')