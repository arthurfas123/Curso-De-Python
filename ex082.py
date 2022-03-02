print('Dividindo valores em varias listas!!!')
print('=-=' * 15)
n = []
pares = []
impares = []
while True:
    continuar = 's'
    n.append(int(input('Digite um valor: ')))
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
        print('=-=' * 15)
        if continuar not in 'SN':
            print('Valor invalido... Tente novamente!')
    if continuar in 'N':
        break
for c in n:
    if c % 2 == 0:
        pares.append(c)
    elif c % 2 != 0:
        impares.append(c)
print(f'Os numeros digitados foram {n}.')
print(f'IMPARES: {impares}')
print(f'PARES: {pares}')
