print('ANALIZANDO UMA PA!!!')
print('=-=' * 15)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = pt
cont = 0
print('=-=' * 15)
while cont < 10:
    cont += 1
    if cont == 1:
        print(f'{pt}', end=' = ')
    else:
        pa += razao
        if cont == 10:
            print(f'{pa}', end='')
        else:
            print(f'{pa}', end=' = ')
