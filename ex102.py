def fatorial(n, show=False):
    """
    => Função para calcular a fotorial de um numero.
    :param n: Numero a ser fatorado.
    :param show: (Opcional) Valor que decide se sera mostrado o processo de fatoração na tela.
    :return: retorna o resultado da fatoração de um numero e seu processo de fatoração.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
    return f


numero = int(input('Digite um numero para ver sua fatorial: '))
show = str(input('Deseja ver o processo de fatoração [S/N]: ')).upper().strip()[0]
if show in 'N':
    print('=-=' * 15)
    print(fatorial(numero, show=False))
else:
    print('=-=' * 15)
    print(fatorial(numero, show=True))
