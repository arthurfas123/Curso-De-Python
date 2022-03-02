print('Mais sobre matriz!!!')
print('=-=' * 15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = scoluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            scoluna += matriz[l][c]
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]
    print()
print('=-=' * 15)
print(f'Soma dos valores pares: {par}')
print(f'Soma dos valores da 3 coluna: {scoluna}')
print(f'Maior valor da segunda linha: {maior}')
