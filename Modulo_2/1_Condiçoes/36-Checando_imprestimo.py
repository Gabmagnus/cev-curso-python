vimp = float(input('Valor da casa: '))
vslr = float(input('Salário do comprador: '))
tmp = float(input('Tempo de pagamento(Em anos): '))
lim = vslr*30/100

if vimp/(tmp*12) > lim:
    print('Imprestimo recusado')
else:
    print('Imprestimo aprovado!')





