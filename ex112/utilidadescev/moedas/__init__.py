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
    print(f'Preço Analizado: \t{formatando(valor)}')
    print(f'Dobro: \t\t\t\t{dobro(valor, True)}')
    print(f'Metade: \t\t\t{metade(valor, True)}')
    print(f'Aumentando {mais}%: \t{aumentar(valor, mais, True)}')
    print(f'Diminuindo {menos}%: \t{diminuir(valor, menos, True)}')
