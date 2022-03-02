def aumentar(valor=0, taxa=0):
    valor += valor * taxa/100
    return valor


def diminuir(valor=0, taxa=0):
    valor -= valor * taxa/100
    return valor


def dobro(valor=0):
    valor *= 2
    return valor


def metade(valor=0):
    valor /= 2
    return valor


def linha():
    print('=-=' * 15)


def formatando(valor=0, moedas='R$'):
    return f'{moedas}{valor:.2f}'.replace('.', ',')

