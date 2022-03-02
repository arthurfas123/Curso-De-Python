print('CALCULANDO FATORIAL!!!')
print('=-=' * 15)
n1 = int(input('Digite um numero: '))
cont = n1
f = 1
print('=-=' * 15)
print(f'{n1}! = ', end='')
while cont > 0:
    print(f'{cont}', end=' ')
    print('X' if cont > 1 else '=', end=' ')
    f *= cont
    cont -= 1
print(f'{f}')
