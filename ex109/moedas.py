def aumentar(valor=0, taxa=0, formato=False):
    valor += valor * taxa/100
    return valor if formato is False else formatando(valor)


def diminuir(valor=0, taxa=0, formato=False):
    valor -= valor * taxa/100
    return valor if formato is False else formatando(valor)


def dobro(valor=0, formato=False):
    valor *= 2
    return valor if formato is False else formatando(valor)


def metade(valor=0, formato=False):
    valor /= 2
    return valor if formato is False else formatando(valor)


def linha():
    print('=-=' * 15)


def formatando(valor=0, moedas='R$'):
    return f'{moedas}{valor:.2f}'.replace('.', ',')

