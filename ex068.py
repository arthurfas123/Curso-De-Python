from random import randint
print('PAR OU IMPAR!!!')
print('=-=' * 15)
cont = 0
while True:
    computador = randint(0, 10)
    pi = str(input('Par ou impar [P/I]: ')).upper().strip()[0]
    jogador = int(input('Numero: '))
    print('=-=' * 15)
    if pi not in 'PI':
        print(f'\033[31mOPÇÃO ({pi}) INVALIDA!\033[m')
        print('=-=' * 15)
    if pi in 'P':
        print('Você escolheu par.')
    elif pi in 'I':
        print('VOCÊ escolheu impar.')
    print(f'Você jogou {jogador} e o computador {computador} = {jogador + computador}')
    print('=-=' * 15)
    if 'P' in pi:
        if (computador + jogador) % 2 == 0:
            cont += 1
            print('PARABÉNS VOCÊ GANHOU!!! tente ganhar de novo.')
        elif (computador + jogador) % 2 != 0:
            print(f'VOCÊ PERDEU!!! você ganhou {cont} vezes.')
            break
    if 'I' in pi:
        if (computador + jogador) % 2 == 0:
            print(f'VOCÊ PERDEU!!! você ganhou {cont} vezes.')
            break
        elif (computador + jogador) % 2 != 0:
            cont += 1
            print('VOCÊ GANHOU!!! tente ganhar de novo.')
