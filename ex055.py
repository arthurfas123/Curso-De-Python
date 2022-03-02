print('MAIOR E MENOR PESO!!!')
print('=-=' * 15)
cont = maior = menor = 0
for c in range(1, 6):
    n = int(input(f'Peso da {c} pessoa: Kg'))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif cont > 1:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('=-=' * 15)
print(f'MAIOR: Kg {maior}')
print(f'MENOR: Kg {menor}')
