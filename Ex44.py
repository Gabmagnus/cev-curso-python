v = float(input('Preço das compras: BRL'))
t = int(input('[ 1 ] à vista no dinheiro\n'
              '[ 2 ] à vista no cartão\n'
              '[ 3 ] 2x no cartão\n'
              '[ 4 ] 3x ou mais no cartão\n'
              'Digite sua opção: '))

vavstd = v - (v*10/100)
vavstc = v - (v*5/100)
vparc = v + (v*20/100)
if t == 1:
    print('Sua compra de {:.2f}, custará {:.2f} a vista no dinheiro'.format(v, vavstd))
elif t == 2:
    print('Sua compra de {:.2f}, custará {:.2f} a vista no cartão'.format(v, vavstc))
elif t == 3:
    print('Sua compra de {:.2f}, não é alterada e custará {:.2f} 2x no cartão'.format(v, v))
elif t == 4:
    qtd = input('Quantas parcelas?')
    print('Sua compra de {:.2f}, custará {:.2f} em {}x no cartao'.format(v, vparc, qtd))
else:
    print('Valor invalido!!')