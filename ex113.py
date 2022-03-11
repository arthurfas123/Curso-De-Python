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


def leiaFloat(msg=''):
    while True:
        n = str(input(msg))
        try:
            n = float(n)
        except Exception as erro:
            print(f'\033[31mErro: \"{n}\" Valor Real invalido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'O usuario preferiu não informar o valor!')
        else:
            return n


inteiro = leiaInt('Digite um valor inteiro: ')
real = leiaFloat('Digite um valor Real: ')
print(f'Você digitou o valor Inteiro {inteiro}, e o valor Real {real}.')
