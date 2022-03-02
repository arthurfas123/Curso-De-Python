print('LISTAS!!!')
print('=-=' * 15)
n = []
maior = menor = 0
for c in range(0, 5):
    n.append(int(input(f'{c} Numero: ')))
maior = n[0]
menor = n[0]
for c in n:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print('=-=' * 15)
for i, v in enumerate(n):
    if v == maior:
        print(f'Maior valor: {maior}, Indice {i}.')
    if v == menor:
        print(f'Menor valor: {menor}, Indice {i}.')
