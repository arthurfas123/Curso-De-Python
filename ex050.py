print('SOMANDO 6 VALORES!!!')
print('=-=' * 15)
n = []
m = []
for c in range(1, 7):
    n.append(int(input(f'{c} NUMERO: ')))
print('=-=' * 15)
soma = 0
for c in n:
    if c % 2 == 0:
        m.append(c)
        soma += c
print(f'A soma dos numeros pares {m} são {soma}')
