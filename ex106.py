from time import sleep
c = ('\033[m',         # 0 sem cor
     '\033[0;31;40m',  # 1 vermelho
     '\033[0;32;40m',  # 2 verde
     '\033[7;40m',      # 3 branco
     '\033[0;34;40m'    # 4 azul
    )


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    titulo('Sistema de ajuda PyHelp!', 2)
    comando = str(input('função ou Biblioteca > '))
    if comando.upper() in 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo!', 1)
