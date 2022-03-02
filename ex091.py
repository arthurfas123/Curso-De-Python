from random import randint
from time import sleep
from operator import itemgetter
print('Jogando dados com dicionarios!!!')
print('=-=' * 15)
jogadores = {'Jogador 1': randint(0, 6),
             'Jogador 2': randint(0, 6),
             'Jogador 3': randint(0, 6),
             'Jogador 4': randint(0, 6)}
ranking = list()
print(f'Os numeros sorteados foram:')
for k, v in jogadores.items():
    print(f'{k}: {v}')
    sleep(1)
print('=-=' * 15)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING":>23}')
print('=-=' * 15)
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]}, Pontos {v[1]}')
    sleep(1)
