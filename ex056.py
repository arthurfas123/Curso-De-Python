print('ANALISADOR COMPLETO!!!')
print('=-=' * 15)
media = 0
nomevelho = ''
idadevelho = 0
m20 = 0
for c in range(1, 5):
    print(f'{c} PESSOA...')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: ')).upper().strip()
    media += idade
    if c == 1:
        nomevelho = nome
        idadevelho = idade
    if idade > idadevelho and sexo in 'M':
        nomevelho = nome
        idadevelho = idade
    if sexo in 'F' and idade < 20:
       m20 += 1
    print('=-=' * 15)
print(f'Media de idade: {media / 4:.2f}')
print(f'Homen mais velho: {nomevelho}, Idade {idadevelho}.')
print(f'Mulheres menores de 20 anos: {m20}.')
