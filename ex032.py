from datetime import date
print('Ano bissexto!!!')
print('=-=' * 20)
ano = int(input('Digite um ano qualquer (aperte 0 para pegar o ano atual): '))
print('=-=' * 20)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
