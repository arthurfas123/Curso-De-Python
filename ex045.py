from random import choice
print('=-=' * 15)
print('                 JOKENPÔ')
print('=-=' * 15)
n = ('PEDRA', 'PAPEL', 'TESOURA')
pc = choice(n)
print('''Escolha entre:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Qual deseja jogar: '))
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
else:
    jogador = 'TESOURA'
print('=-=' * 15)
print(f'               {jogador} X {pc}')
print('=-=' * 15)
if jogador == 'PEDRA':
    if pc == 'PEDRA':
        print('PARECE QUE EMPATAMOS!!! MAIS SORTE NA PROXIMA.')
    elif pc == 'PAPEL':
        print('SINTO MUITO!!! EU GANHEI, MAIS SORTE NA PROXIMA.')
    elif pc == 'TESOURA':
        print('PARABÉNS!!! VOCÉ GANHOU.')
elif jogador == 'PAPEL':
    if pc == 'PEDRA':
        print('PARABÉNS!!! VOCÉ GANHOU.')
    elif pc == 'PAPEL':
        print('PARECE QUE EMPATAMOS!!! MAIS SORTE NA PROXIMA.')
    elif pc == 'TESOURA':
        print('SINTO MUITO!!! EU GANHEI, MAIS SORTE NA PROXIMA.')
elif jogador == 'TESOURA':
    if pc == 'PEDRA':
        print('SINTO MUITO!!! EU GANHEI, MAIS SORTE NA PROXIMA.')
    elif pc == 'PAPEL':
        print('PARABÉNS!!! VOCÉ GANHOU.')
    elif pc == 'TESOURA':
        print('PARECE QUE EMPATAMOS!!! MAIS SORTE NA PROXIMA.')
