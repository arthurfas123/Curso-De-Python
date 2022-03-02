print('Aproveitamento de um jogador!!!')
print('=-=' * 15)
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Numero De Partidas'] = int(input('Numero De partidas: '))
print('=-=' * 15)
dados['Numero De Gols'] = []
dados['Total de gols'] = 0
for c in range(0, dados['Numero De Partidas']):
    dados['Numero De Gols'].append(int(input(f'Numero de gols na {c} partida: ')))
    dados['Total de gols'] += dados['Numero De Gols'][c]
print('=-=' * 30)
print(dados)
print('=-=' * 30)
for k, v in dados.items():
    print(f'{k}: \033[34m{v}\033[m')
print('=-=' * 15)
print(f'O jogador {dados["Nome"]} jogou {dados["Numero De Partidas"]} Partidas.')
for c in range(0, dados['Numero De Partidas']):
    print(f'    ==> Partida {c}: \033[34m{dados["Numero De Gols"][c]}\033[m Gols.')
print(f'    ==> Total De Gols: \033[34m{dados["Total de gols"]}\033[m')
