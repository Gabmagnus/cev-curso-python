from datetime import datetime

y = int(input('Ano de nascimento: '))
age = datetime.today().year - y

if age > 18:
    print('Deveria ter servido a {} anos!'.format(age-18))
elif age < 18:
    print('Deverá servir a {} anos!'.format(18-age))
else:
    print('Deve servir este ano!')
