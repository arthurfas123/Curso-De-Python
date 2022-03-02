from random import randint
print('GERANDO NUMEROS ALEATORIOS E COLOCANDO EM TUPLAS!!!')
print('=-=' * 15)
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Numeros sorteados: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
