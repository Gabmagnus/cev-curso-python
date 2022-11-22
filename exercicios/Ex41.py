from datetime import datetime

y = int(input('Ano de nascimento: '))
age = datetime.today().year - y

if age <= 9:
    r = 'MIRIM'
elif age > 9 and age <= 14:
    r = 'INFANTIL'
elif age > 14 and age <= 19:
    r = 'Junior'
elif age > 19 and age <= 25:
    r = 'Senior'
else:
    r = 'Master'

print('Com {} anos você é um atleta {}'.format(age, r))
