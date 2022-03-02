from time import sleep


def maior(*n):
    maior = 0
    print('Analizando Valores...')
    for c in n:
        print(c, end=' ', flush=True)
        sleep(0.5)
        if c > maior:
            maior = c
    print(f'Foram informados {len(n)} valores.')
    print(f'Maior numero: {maior}')
    print('=-=' * 15)


maior(9, 3, 5, 2)
maior(0, 1, 3)
maior()
maior(19, 7)
