from datetime import date
data = date.today().year
print('Alistamento militar!!!')
print('=-=' * 20)
ano = int(input('Ano De Nascimento: '))
idade = data - ano
print('=-=' * 20)
if idade > 18:
    print(f'Ja passou do ano de alistamento. Você esta {idade - 18} anos atrasado!')
elif idade < 18:
    print(f'Ainda falta {18 - idade} anos para o alistamento!')
elif idade == 18:
    print(f'Parabéns! esta na sua vez, apresente-se na junta militar mais proxima com seus documentos em mãos!')
