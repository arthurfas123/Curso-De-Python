print('SOMANDO VARIOS VALORES!!!')
print('=-=' * 15)
n1 = 0
cont = 0
soma = 0
while n1 != 999:
    soma += n1
    cont += 1
    print('Digite 999 para finalizar.')
    n1 = int(input(f'{cont} Numero: '))
    print('=-=' * 15)
print(f'foram digitados {cont - 1} valores.')
print(f'A soma desses valores vale {soma}.')
