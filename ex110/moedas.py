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


def formatando(valor=0, moedas='R$'):
    return f'{moedas}{valor:.2f}'.replace('.', ',')


def titulo(msg):
    print('-' * 32)
    print(f'        {msg}')
    print('-' * 32)


def resumo(valor=0, mais=0, menos=0):
    titulo('Resumo Do Valor')
    print(f'Preço Analizado: {formatando(valor):>13}')
    print(f'Dobro: {dobro(valor, True):>23}')
    print(f'Metade: {metade(valor, True):>22}')
    print(f'Aumentando {mais}%: {aumentar(valor, mais, True):>14}')
    print(f'Diminuindo {menos}%: {diminuir(valor, menos, True):>14}')
