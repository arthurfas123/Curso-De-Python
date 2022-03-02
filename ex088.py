from random import randint
from time import sleep
print('Mega sena!!!')
print('=-=' * 15)
jogos = []
njogos = int(input('Quantos jogos deseja gerar: '))
print('=-=' * 15)
for c in range(0, njogos):
    jogos.append([])
    while len(jogos[c]) < 6:
        palpite = randint(1, 60)
        if palpite not in jogos[c]:
            jogos[c].append(palpite)
for c in range(0, len(jogos)):
    jogos[c].sort()
    print(f'{c + 1} Jogo: {jogos[c]}')
    sleep(1)
