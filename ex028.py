from random import randint
print('\033[31m=-=' * 20)
print(' ' * 15, '\033[34mJOGO DA ADIVINHAÇÂO!!!')
print('\033[31m=-=' * 20)
n = randint(0, 5)
print('\033[34mEstou penssando em um numero entre 0 E 5.')
print(f' ' * 10, 'Tente Adivinhar!')
print('\033[31m=-=' * 20)
jogador = int(input('\033[34mQual seu palpite: '))
print('\033[31m=-=' * 20)
novojogo = ''
if jogador == n:
    print('\033[34mPARABÉNS!!! VOCÊ ACERTOU.')
else:
    while True:
        if novojogo == 'N':
            break
        elif jogador == n:
            print('\033[34mPARABÉNS!!! VOCÊ ACERTOU.')
            break
        else:
            novojogo = str(input('\033[34mVOCÊ ERROU!!! QUER TENTAR DE NOVO? ')).upper().strip()
            print('\033[31m=-=' * 20)
            if novojogo[0] == 'S':
                jogador = int(input('\033[34mQual seu novo palpíte: '))
                print('\033[31m=-=' * 20)
print('\033[34mAGRADEÇO PELA PARTIDA! ATÉ A PROXIMA.')
