from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    cont = i
    print(f'Contando de {i} a {f} de {p} em {p}:')
    sleep(2.5)

    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print()
        print('=-=' * 15)
    else:
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print()


contador(0, 10, 1)
contador(0, 10, 2)
inicio = int(input('INICIO: '))
fim = int(input('FIM:       '))
passo = int(input('PASSO:   '))
print('=-=' * 15)
contador(inicio, fim, passo)
