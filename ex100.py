from random import randint
from time import sleep


def sorteia(lista):
    print('=-=' * 15)
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in lista:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
    print()


def somapar(lista):
    soma = 0
    for c in n:
        if c % 2 == 0:
            soma += c
    print(f'Soma dos valores pares: {soma}')


n = []
sorteia(n)
somapar(n)
