print('SEQUENCIA DE FIBONACCI!!!')
print('=-=' * 15)
n = int(input('Quantos termos deseja ver: '))
cont = 0
n1 = 0
n2 = 1
n3 = 0
print('=-=' * 15)
while cont < n:
    print(f'{n1}', end=' = ')
    cont += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if cont == n:
        print('FIM...')
