print('Maior e Menor valor!!!')
print('=-=' * 20)
lista = []
menor = maior = count = 0
for c in range(0, 3):
    lista.append(int(input(f'Digite o {c + 1} numero: ')))
for c in lista:
    count += 1
    if c > maior:
        maior = c
    if count == 1:
        menor = c
    elif c < menor:
        menor = c
print('=-=' * 20)
print(f'Menor: {menor}')
print(f'maior: {maior}')
