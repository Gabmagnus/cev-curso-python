# na e o numero de ( == ) se nao errado
e = str(input('Digite a expressao: '))

paren = 0
pareninv = 0
for c in range(0, len(e)):
    if e[c] == '(':
        paren += 1
    elif e[c] == ')':
        pareninv += 1

if paren == pareninv:
    print('Esta expressao é VALIDA!')
else:
    print('Esta opçao é INVALIDA')

