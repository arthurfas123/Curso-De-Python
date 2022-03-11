def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg=''):
    while True:
        n = str(input(msg))
        try:
            n = int(n)
        except Exception as erro:
            print(f'\033[31mErro: \"{n}\" Valor inteiro invalido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'O usuario preferiu não informar o valor.')
        else:
           return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc