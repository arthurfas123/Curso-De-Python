from random import randint
print('JOGO DA ADIVINHAÇÃO!!!')
print('=-=' * 15)
print('Estou pensando em um numero entre 1 e 10.')
print('Tente adivinhar.')
print('=-=' * 15)
n = randint(1, 10)
cont = 0
while True:
    cont += 1
    jogador = int(input('Seu palpite: '))
    if jogador == n:
        print('=-=' * 15)
        print('PARABÉNS!!! VOCÊ VENCEU.')
        print(f'Vocé usou {cont} palpites.')
        break
    else:
        print('VOCÉ ERROU!!! TENTE DE NOVO.')
        print('=-=' * 15)
