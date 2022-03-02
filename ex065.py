print('MAIOR E MENOR VALOR!!!')
print('=-=' * 15)
cont = soma = maior = menor = 0
continuar = ''
while True:
    cont += 1
    n1 = int(input(f'{cont} Numero: '))
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    soma += n1
    continuar = str(input('Deseja digitar outro valor [S/N]: ')).upper().strip()[0]
    print('=-=' * 15)
    if 'N' in continuar:
        break
print(f'Media dos valores inseridos: {soma / cont:.1f}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
