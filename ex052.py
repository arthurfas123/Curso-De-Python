print('IDENTIFICANDO PRIMOS!!!')
print('=-=' * 15)
n = int(input('Digite um numero: '))
print('=-=' * 15)
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print(f'\033[34m{c}\033[m', end=' ')
    else:
        print(c, end=' ')
print('')
print('=-=' * 15)
print(f'O numero {n} foi divisivel {cont} vezes')
if cont > 2:
    print('O numero NÃO é PRIMO.')
else:
    print('O numero É PRIMO.')
