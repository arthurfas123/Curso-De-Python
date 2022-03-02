print('FLAG!!!')
print('=-=' * 15)
continuar = ''
cont = soma = 0
while True:
    cont += 1
    n1 = int(input('Digite um valor: '))
    soma += n1
    continuar = int(input('Deseja continuar (999 p/parar 0 p/continuar): '))
    print('=-=' * 15)
    if continuar == 999:
        break
print(f'Foram inseridos {cont} valores.')
print(f'SOMA: {soma}')
