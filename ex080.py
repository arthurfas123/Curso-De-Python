print('Lista ordenada sem repetição!!!')
print('=-=' * 15)
n = []
cont = 0
for c in range(0, 4):
    n2 = int(input(f'{c} Valor: '))
    if c == 0 or n2 > n[-1]:
        n.append(n2)
    else:
        pos = 0
        while pos < len(n):
            if n2 <= n[pos]:
                n.insert(pos, n2)
                break
            pos += 1
print('=-=' * 15)
print(f'Numeros em ordem crescente: {n}')
