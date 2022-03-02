print('dicionarios dentro de listas!!!')
print('=-=' * 15)
dados = []
usuario = {}
media = 0
while True:
    continuar = 's'
    usuario['NOME'] = str(input('Nome: '))
    while True:
        usuario['SEXO'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if usuario['SEXO'] in 'MF':
            break
        print('OPÇÃO INVALIDA... TENTE NOVAMENTE!')
        print('=-=' * 15)
    usuario['IDADE'] = int(input('Idade: '))
    media += usuario['IDADE']
    dados.append(usuario.copy())
    usuario.clear()
    while continuar not in 'SN':
        continuar = str(input('Cadastrar novo usuario [S/N]: ')).upper().strip()[0]
        print('=-=' * 15)
        if continuar not in 'SN':
            print('OPÇÃO INVALIDA... TENTE NOVAMENE!')
            print('=-=' * 15)
    if continuar in 'N':
        break
media = media / len(dados)
print(f'Foram cadastrados {len(dados)} Usuarios.')
print(f'Media De Idade: {media:.0f}.')
print(f'Mulheres:', end=' ')
for c in dados:
    if c['SEXO'] == 'F':
        print(f'{c["NOME"]}', end=', ')
print()
print(f'Usuarios acima Da media de idade:', end=' ')
for c in dados:
    if c['IDADE'] > media:
        print(f'{c["NOME"]}', end=', ')
print()
