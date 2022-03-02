print('Lista composta e analise de dados!!!')
print('=-=' * 15)
dados = list()
pessoa = list()
pgordo = pmagro = 0
while True:
    continuar = 's'
    pessoa.append(str(input('NOME: ')))
    pessoa.append(str(input('PESO: ')))
    if len(dados) == 0:
        pgordo = pmagro = pessoa[1]
    else:
        if pessoa[1] > pgordo:
            pgordo = pessoa[1]
        if pessoa[1] < pmagro:
            pmagro = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
        print('=-=' * 15)
        if continuar not in 'SN':
            print('OPÇAO INVALIDA... TENTE NOVAMENTE!')
    if continuar in 'N':
        break
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'Pessoas mais pesadas: ', end='')
for c in dados:
    if c[1] == pgordo:
        print(f'{c[0]}', end=', ')
print(f'Com Kg{pgordo}')
print(f'Pessoas mais leves: ', end='')
for c in dados:
    if c[1] == pmagro:
        print(f'{c[0]}', end=', ')
print(f'Com Kg{pmagro}')
