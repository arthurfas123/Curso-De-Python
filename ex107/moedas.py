def aumentar(valor, taxa):
    valor += valor * taxa/100
    return valor


def diminuir(valor, taxa):
    valor -= valor * taxa/100
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2
    return valor


def linha():
    print('=-=' * 15)
