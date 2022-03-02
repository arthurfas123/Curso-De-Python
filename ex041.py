from datetime import date
data = date.today().year
print('Classificando atletas!!!')
print('=-=' * 20)
ano = int(input('Ano de nascimento: '))
idade = data - ano
print('=-=' * 20)
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIN!')
elif 9 < idade <= 14:
    print('INFANTIL!')
elif 14 < idade <= 19:
    print('JUNIOR!')
elif 19 < idade <= 25:
    print('SENIOR!')
elif idade > 25:
    print('MASTER!')
