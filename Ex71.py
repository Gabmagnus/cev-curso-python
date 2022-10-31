vlr = float(input('Qual valor voce quer sacar? RS'))
notas = [50, 20, 10, 1]
valores = [0, 0, 0, 0]
count = 0
c = 0
while count <= 3:
    if vlr % notas[count] == 0:
        valores[count] = vlr // notas[count]
        print('Total de {:.0f} cédulas de RS{}'.format(valores[count], notas[count]))
        break

    elif vlr % notas[count] != 0 and vlr % notas[count] > 1:
        valores[count] = vlr // notas[count]
        vlr = vlr % notas[count]

    elif vlr % notas[count] != 0 and vlr % notas[count] < 1:
        valores[count] = vlr


    if valores[count] == 0:
        print('Total de {:.0f} cédulas de RS{}'.format(valores[count], notas[count]))

    count += 1
