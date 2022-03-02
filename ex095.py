print('Aprimorando dicionarios!!!')
print('=-=' * 15)
dados = dict()
jogadores = list()
while True:
    dados['nome'] = str(input('NOME: '))
    npartidas = int(input('Numero De Partidas: '))
    dados['gols por partida'] = []
    dados['total de gols'] = 0
    print('=-=' * 15)
    for c in range(0, npartidas):
        dados['gols por partida'].append(int(input(f'Gols Na {c} Partida: ')))
        dados['total de gols'] += dados['gols por partida'][c]
    print('=-=' * 15)
    while True:
        continuar = str(input('Cadastrar novo jogador [S/N]: ')).upper().strip()[0]
        print('=-=' * 15)
        if continuar in 'SN':
            break
        print('OPÇÃO INVALIDA... TENTE NOVAMENTE!')
    jogadores.append(dados.copy())
    dados.clear()
    if continuar in 'N':
        break
print(f'{"COD":<4}{"NOME":<8}{"GOLS":>7}{"TOTAL":>10}')
print('=-=' * 15)
for i, v in enumerate(jogadores):
    print(f'{i}', end='  ')
    for n in v.values():
        print(f'{n}', end='    ')
    print()
print('=-=' * 15)
while True:
    while True:
        continuar = str(input('Deseja ver algum desempenho [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
    p = int(input('Qual jogador deseja ver o desempenho: '))
    if p < len(jogadores) - 1:
        print('=-=' * 15)
        print(f'  ==> Desempenho Do Jogador: {jogadores[p]["nome"].upper()}')
        for i, v in enumerate(jogadores[p]["gols por partida"]):
            print(f'   ==> {i} Partida: {v} Gols.')
        print('=-=' * 15)
    else:
        print('OPÇÃO INVALIDA... TENTE NOVAMENTE!')
        print('=-=' * 15)
print('FINALIZANDO...')
