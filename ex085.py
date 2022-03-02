print('Lista com pares e impares!!!')
print('=-=' * 15)
numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'{c} VALOR: '))
    if n % 2 == 0:
        numeros[1].append(n)
    else:
        numeros[0].append(n)
numeros[0].sort()
numeros[1].sort()
print('=-=' * 15)
print(f'PAR: {numeros[1]}')
print(f'IMPAR: {numeros[0]}')
